#!/bin/bash

################################################################################
# Data Visual Chronicle - Video Renderer
# Automated video rendering script for MacBook
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

    echo ""

    if [ "$all_good" = false ]; then
        print_error "Prerequisites not met. Please install missing dependencies."
        echo ""
        print_info "Quick install commands:"
        echo "  brew install node"
        echo "  brew install ffmpeg"
        echo ""
        exit 1
    fi

    print_success "All prerequisites met!"
    echo ""
}

################################################################################
# Install Dependencies
################################################################################

install_dependencies() {
    print_step "Checking Node.js dependencies..."
    echo ""

    if [ -d "node_modules" ]; then
        print_info "node_modules directory exists"
        read -p "Do you want to reinstall dependencies? (y/N): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Removing old node_modules..."
            rm -rf node_modules package-lock.json
            print_step "Installing dependencies (this may take 2-5 minutes)..."
            npm install
        else
            print_success "Using existing dependencies"
        fi
    else
        print_step "Installing dependencies (this may take 2-5 minutes)..."
        npm install
    fi

    if [ $? -eq 0 ]; then
        print_success "Dependencies installed successfully!"
    else
        print_error "Failed to install dependencies"
        exit 1
    fi
    echo ""
}

################################################################################
# Create Output Directory
################################################################################

setup_output_directory() {
    print_step "Setting up output directory..."

    if [ ! -d "$OUTPUT_DIR" ]; then
        mkdir -p "$OUTPUT_DIR"
        print_success "Created output directory: $OUTPUT_DIR/"
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

    print_info "Composition: $COMPOSITION"
    print_info "Output: $OUTPUT_DIR/${VIDEO_NAME}.mp4"
    print_info "Duration: 4:00 minutes (7,200 frames)"
    print_info "Resolution: 1920x1080 (Full HD)"
    print_info "Codec: H.264"
    echo ""

    # Detect CPU cores for optimal concurrency
    CPU_CORES=$(sysctl -n hw.ncpu 2>/dev/null || echo "4")
    CONCURRENCY=$((CPU_CORES / 2))
    if [ $CONCURRENCY -lt 1 ]; then
        CONCURRENCY=1
    fi

    print_info "Detected $CPU_CORES CPU cores, using concurrency: $CONCURRENCY"
    echo ""

    print_warning "This will take approximately 20-60 minutes depending on your Mac."
    print_info "Please keep your Mac plugged in and don't close the terminal."
    echo ""

    read -p "Press ENTER to start rendering (or Ctrl+C to cancel)..."
    echo ""

    print_step "Rendering video... (you can monitor progress below)"
    echo ""

    # Start timer
    START_TIME=$(date +%s)

    # Render the video
    npx remotion render $COMPOSITION "$OUTPUT_DIR/${VIDEO_NAME}.mp4" \
        --codec h264 \
        --concurrency $CONCURRENCY \
        --overwrite

    RENDER_EXIT_CODE=$?

    # End timer
    END_TIME=$(date +%s)
    DURATION=$((END_TIME - START_TIME))
    MINUTES=$((DURATION / 60))
    SECONDS=$((DURATION % 60))

    echo ""

    if [ $RENDER_EXIT_CODE -eq 0 ]; then
        print_success "Video rendered successfully!"
        echo ""
        print_info "Render time: ${MINUTES}m ${SECONDS}s"
        print_info "Output file: $OUTPUT_DIR/${VIDEO_NAME}.mp4"

        # Get file size
        if [ -f "$OUTPUT_DIR/${VIDEO_NAME}.mp4" ]; then
            FILE_SIZE=$(du -h "$OUTPUT_DIR/${VIDEO_NAME}.mp4" | cut -f1)
            print_info "File size: $FILE_SIZE"
        fi

        echo ""
        return 0
    else
        print_error "Video rendering failed!"
        echo ""
        print_info "Check the error messages above for details."
        print_info "Common issues:"
        echo "  - Port 3000 in use (kill with: lsof -ti:3000 | xargs kill -9)"
        echo "  - Insufficient memory (close other applications)"
        echo "  - Missing data files (check public/assets/ directory)"
        echo ""
        return 1
    fi
}

################################################################################
# Open Video
################################################################################

open_video() {
    echo ""
    read -p "Do you want to open the video now? (Y/n): " -n 1 -r
    echo ""

    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        if [ -f "$OUTPUT_DIR/${VIDEO_NAME}.mp4" ]; then
            print_step "Opening video..."
            open "$OUTPUT_DIR/${VIDEO_NAME}.mp4"
            print_success "Video opened in default player"
        else
            print_error "Video file not found: $OUTPUT_DIR/${VIDEO_NAME}.mp4"
        fi
    fi
}

################################################################################
# Cleanup Function
################################################################################

cleanup_on_exit() {
    echo ""
    print_warning "Script interrupted. Cleaning up..."
    exit 130
}

################################################################################
# Main Script
################################################################################

main() {
    # Trap Ctrl+C
    trap cleanup_on_exit INT

    # Clear screen and show header
    clear
    print_header

    # Run checks and setup
    check_prerequisites
    install_dependencies
    setup_output_directory

    # Render video
    render_video
    RENDER_SUCCESS=$?

    # Show results
    if [ $RENDER_SUCCESS -eq 0 ]; then
        echo ""
        echo -e "${GREEN}"
        echo "╔════════════════════════════════════════════════════════════════╗"
        echo "║                                                                ║"
        echo "║                    ✓ SUCCESS!                                  ║"
        echo "║                                                                ║"
        echo "║     Your video is ready at: $OUTPUT_DIR/${VIDEO_NAME}.mp4"
        echo "║                                                                ║"
        echo "╚════════════════════════════════════════════════════════════════╝"
        echo -e "${NC}"

        # Open video
        open_video

        echo ""
        print_info "Next steps:"
        echo "  1. Review the video"
        echo "  2. Upload to YouTube"
        echo "  3. Share with the world! 🎉"
        echo ""
    else
        echo ""
        echo -e "${RED}"
        echo "╔════════════════════════════════════════════════════════════════╗"
        echo "║                                                                ║"
        echo "║                    ✗ FAILED                                    ║"
        echo "║                                                                ║"
        echo "║            Video rendering was not successful.                 ║"
        echo "║                                                                ║"
        echo "╚════════════════════════════════════════════════════════════════╝"
        echo -e "${NC}"
        echo ""
        print_info "Troubleshooting tips:"
        echo "  1. Check error messages above"
        echo "  2. Read MAC_SETUP_GUIDE.md for detailed help"
        echo "  3. Try running with verbose logging:"
        echo "     npx remotion render $COMPOSITION $OUTPUT_DIR/${VIDEO_NAME}.mp4 --log=verbose"
        echo ""
        exit 1
    fi
}

# Run main function
main
