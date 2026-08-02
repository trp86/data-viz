#!/bin/bash

################################################################################
# Data Visual Chronicle - Complete Video Renderer
# Automated data processing and video rendering script for MacBook
################################################################################

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
VIDEO_NAME="healthy-diet-video"
OUTPUT_DIR="out"
COMPOSITION="VideoComposition"
PARENT_DIR=".."
VENV_DIR="$PARENT_DIR/venv"

################################################################################
# Helper Functions
################################################################################

print_header() {
    echo -e "${CYAN}"
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                                                                ║"
    echo "║           📊 Data Visual Chronicle - Video Renderer            ║"
    echo "║                                                                ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_step() {
    echo -e "${MAGENTA}➜ $1${NC}"
}

################################################################################
# Check Prerequisites
################################################################################

check_prerequisites() {
    echo ""
    print_step "Checking prerequisites..."
    echo ""

    local all_good=true

    # Check Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python installed: $PYTHON_VERSION"
    else
        print_warning "Python3 is not installed (optional for data processing)"
        echo "  Install with: brew install python3"
    fi

    # Check Node.js
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node --version)
        print_success "Node.js installed: $NODE_VERSION"
    else
        print_error "Node.js is not installed!"
        echo "  Install with: brew install node"
        all_good=false
    fi

    # Check npm
    if command -v npm &> /dev/null; then
        NPM_VERSION=$(npm --version)
        print_success "npm installed: v$NPM_VERSION"
    else
        print_error "npm is not installed!"
        all_good=false
    fi

    # Check FFmpeg
    if command -v ffmpeg &> /dev/null; then
        FFMPEG_VERSION=$(ffmpeg -version | head -n1 | cut -d' ' -f3)
        print_success "FFmpeg installed: $FFMPEG_VERSION"
    else
        print_error "FFmpeg is not installed!"
        echo "  Install with: brew install ffmpeg"
        all_good=false
    fi

    # Check if in correct directory
    if [ ! -f "package.json" ]; then
        print_error "package.json not found!"
        echo "  Please run this script from the healthydiet-video directory"
        all_good=false
    fi

    if [ "$all_good" = false ]; then
        print_error "Prerequisites not met. Please install missing dependencies."
        echo ""
        print_info "Quick install commands:"
        echo "  brew install node"
        echo "  brew install ffmpeg"
        echo "  brew install python3  # optional for data processing"
        echo ""
        exit 1
    fi

    print_success "All prerequisites met!"
    echo ""
}

################################################################################
# Python Virtual Environment Setup
################################################################################

setup_python_venv() {
    print_step "Checking Python virtual environment..."
    echo ""

    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        print_warning "Python3 not found, skipping virtual environment setup"
        return 0
    fi

    # Check if venv exists
    if [ -d "$VENV_DIR" ]; then
        print_success "Python virtual environment exists at: $VENV_DIR"

        # Activate virtual environment
        print_info "Activating virtual environment..."
        source "$VENV_DIR/bin/activate"

        if [ $? -eq 0 ]; then
            print_success "Virtual environment activated"
            PYTHON_VENV_ACTIVE=true
        else
            print_warning "Failed to activate virtual environment"
            PYTHON_VENV_ACTIVE=false
        fi
    else
        print_info "Virtual environment not found at: $VENV_DIR"
        echo ""
        read -p "Do you want to create Python virtual environment for data processing? (y/N): " -n 1 -r
        echo ""

        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_step "Creating Python virtual environment..."
            cd "$PARENT_DIR"
            python3 -m venv venv

            if [ $? -eq 0 ]; then
                print_success "Virtual environment created successfully at: $VENV_DIR"

                # Activate it
                source venv/bin/activate
                PYTHON_VENV_ACTIVE=true

                # Upgrade pip first
                print_info "Upgrading pip..."
                pip install --upgrade pip

                # Install requirements if they exist
                if [ -f "requirements.txt" ]; then
                    print_step "Installing Python dependencies from requirements.txt..."
                    pip install -r requirements.txt
                    print_success "Python dependencies installed"
                else
                    print_info "No requirements.txt found. Installing common data science packages..."
                    pip install pandas plotly kaleido openpyxl
                    print_success "Core packages installed (pandas, plotly, kaleido, openpyxl)"
                fi
            else
                print_error "Failed to create virtual environment"
                PYTHON_VENV_ACTIVE=false
            fi

            cd - > /dev/null
        else
            print_info "Skipping virtual environment creation"
            PYTHON_VENV_ACTIVE=false
        fi
    fi

    echo ""
}

################################################################################
# Install Dependencies
################################################################################

install_dependencies() {
    print_step "Checking npm dependencies..."
    echo ""

    if [ ! -d "node_modules" ]; then
        print_info "Dependencies not found. Installing..."
        echo ""
        npm install

        if [ $? -eq 0 ]; then
            print_success "Dependencies installed successfully"
        else
            print_error "Failed to install dependencies"
            exit 1
        fi
    else
        print_success "Dependencies already installed"
    fi

    echo ""
}

################################################################################
# Stop Any Running Servers
################################################################################

stop_running_servers() {
    print_step "Checking for running processes on port 3000..."
    echo ""

    # Try to find process on port 3000
    if lsof -ti:3000 > /dev/null 2>&1; then
        print_warning "Found process running on port 3000"
        print_info "Stopping process..."
        lsof -ti:3000 | xargs kill -9 2>/dev/null

        if [ $? -eq 0 ]; then
            print_success "Process stopped successfully"
            sleep 2
        else
            print_warning "Could not stop process automatically"
            echo ""
            read -p "Continue anyway? (y/N): " -n 1 -r
            echo ""
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                exit 1
            fi
        fi
    else
        print_success "Port 3000 is available"
    fi

    echo ""
}

################################################################################
# Setup Output Directory
################################################################################

setup_output_directory() {
    print_step "Setting up output directory..."
    echo ""

    if [ ! -d "$OUTPUT_DIR" ]; then
        mkdir -p "$OUTPUT_DIR"
        print_success "Output directory created: $OUTPUT_DIR/"
    else
        print_success "Output directory exists: $OUTPUT_DIR/"
    fi

    echo ""
}

################################################################################
# Render Video
################################################################################

render_video() {
    print_step "Starting video render..."
    echo ""

    print_info "Configuration:"
    echo "  • Video name: $VIDEO_NAME.mp4"
    echo "  • Output directory: $OUTPUT_DIR/"
    echo "  • Composition: $COMPOSITION"
    echo "  • Duration: 4:00 minutes"
    echo "  • Resolution: 1920x1080 (Full HD)"
    echo "  • Codec: H.264"
    echo ""

    # Detect CPU cores for optimal concurrency
    if [[ "$OSTYPE" == "darwin"* ]]; then
        CPU_CORES=$(sysctl -n hw.ncpu)
    else
        CPU_CORES=$(nproc 2>/dev/null || echo "4")
    fi

    CONCURRENCY=$((CPU_CORES > 2 ? CPU_CORES - 1 : CPU_CORES))

    print_info "Detected $CPU_CORES CPU cores, using concurrency: $CONCURRENCY"
    echo ""

    print_warning "This will take 20-60 minutes depending on your Mac model"
    print_info "M1/M2/M3 Mac: ~20-30 minutes"
    print_info "Intel Mac: ~40-60 minutes"
    echo ""

    # Record start time
    START_TIME=$(date +%s)

    # Run the render command
    npx remotion render "$COMPOSITION" "$OUTPUT_DIR/$VIDEO_NAME.mp4" \
        --codec h264 \
        --overwrite \
        --concurrency "$CONCURRENCY"

    RENDER_EXIT_CODE=$?

    # Record end time
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    MINUTES=$((DURATION / 60))
    SECONDS=$((DURATION % 60))

    echo ""

    if [ $RENDER_EXIT_CODE -eq 0 ]; then
        print_success "Video rendered successfully!"
        echo ""
        print_info "Render time: ${MINUTES}m ${SECONDS}s"

        # Get file size
        if [ -f "$OUTPUT_DIR/$VIDEO_NAME.mp4" ]; then
            FILE_SIZE=$(du -h "$OUTPUT_DIR/$VIDEO_NAME.mp4" | cut -f1)
            print_info "File size: $FILE_SIZE"
            print_info "Location: $OUTPUT_DIR/$VIDEO_NAME.mp4"
        fi

        echo ""
        return 0
    else
        print_error "Video rendering failed!"
        echo ""
        print_info "Common issues:"
        echo "  • Out of memory: Try reducing --concurrency"
        echo "  • Port conflicts: Run ./render-video.sh again"
        echo "  • Missing assets: Check public/assets/ folder"
        echo ""
        return 1
    fi
}

################################################################################
# Open Video
################################################################################

open_video() {
    echo ""
    read -p "Do you want to open the video? (Y/n): " -n 1 -r
    echo ""

    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        if [ -f "$OUTPUT_DIR/$VIDEO_NAME.mp4" ]; then
            open "$OUTPUT_DIR/$VIDEO_NAME.mp4" 2>/dev/null || xdg-open "$OUTPUT_DIR/$VIDEO_NAME.mp4" 2>/dev/null
            print_success "Opening video..."
        else
            print_error "Video file not found at $OUTPUT_DIR/$VIDEO_NAME.mp4"
        fi
    fi
}

################################################################################
# Print Summary
################################################################################

print_summary() {
    echo ""
    echo -e "${CYAN}"
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                                                                ║"
    echo "║                    ✅  RENDER COMPLETE!                        ║"
    echo "║                                                                ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo ""
    print_success "Your 4-minute video is ready!"
    echo ""
    print_info "Next steps:"
    echo "  1. Review the video: $OUTPUT_DIR/$VIDEO_NAME.mp4"
    echo "  2. Upload to YouTube"
    echo "  3. Share with the world! 🚀"
    echo ""
    print_info "Channel: Data Visual Chronicle"
    print_info "Tagline: Transforming Data into Stories"
    echo ""
}

################################################################################
# Main Execution
################################################################################

main() {
    print_header

    # Run all steps
    check_prerequisites
    setup_python_venv
    install_dependencies
    stop_running_servers
    setup_output_directory
    render_video

    # Check if render was successful
    if [ $? -eq 0 ]; then
        print_summary
        open_video
    else
        echo ""
        print_error "Render failed. Please check the errors above."
        echo ""
        exit 1
    fi
}

# Run main function
main
