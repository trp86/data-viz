# 📂 Repository Structure Guide

## ✅ What Has Been Set Up

Your `data-viz` folder is now a **Git repository** that can contain multiple data visualization projects.

---

## 📁 Current Structure

```
data-viz/                                    # ← ROOT REPOSITORY
├── .git/                                    # Git repository data
├── .gitignore                               # Files to ignore in git
├── README.md                                # Main repository documentation
├── REPOSITORY_STRUCTURE.md                  # This file
│
└── 01-Top30DistrictsInOdisha/              # ← PROJECT 1
    ├── src/                                 # Source code
    │   ├── BarChartRace.tsx
    │   ├── TitleScene.tsx
    │   ├── ThankYouScene.tsx
    │   ├── MilestoneCallout.tsx
    │   ├── Composition.tsx
    │   ├── Root.tsx
    │   ├── theme.ts
    │   ├── dataLoader.ts
    │   └── index.ts
    │
    ├── public/                              # Data files
    │   ├── odisha_district_population_2011.csv
    │   └── race_data.csv
    │
    ├── out/                                 # Rendered videos
    │   └── video.mp4
    │
    ├── node_modules/                        # Dependencies (ignored by git)
    ├── package.json                         # Project dependencies
    ├── tsconfig.json                        # TypeScript config
    ├── remotion.config.ts                   # Remotion settings
    │
    ├── README.md                            # Project documentation
    ├── SETUP_WINDOWS.md                     # Windows setup guide
    └── SETUP_MAC.md                         # Mac setup guide
```

---

## 🎯 Repository Concept

### Root Level (`data-viz/`)
- **One Git repository** for all your visualization projects
- Central README explaining the repository
- Shared .gitignore file
- Each project is a subfolder

### Project Level (`01-Top30DistrictsInOdisha/`)
- **Self-contained projects** with their own:
  - Dependencies (package.json)
  - Source code (src/)
  - Data files (public/)
  - Documentation (README.md)
  - Setup guides (SETUP_*.md)

---

## 📝 Naming Convention

Projects should follow this pattern:

```
XX-ProjectName/
```

Where:
- `XX` = Two-digit number (01, 02, 03...)
- `ProjectName` = Descriptive name in PascalCase or kebab-case

**Examples:**
```
01-Top30DistrictsInOdisha/
02-StateGDPComparison/
03-PopulationGrowthTrends/
04-EducationStatistics/
```

---

## 🚀 Adding New Projects

### Method 1: Copy Existing Project

1. **Duplicate the folder:**
   ```bash
   cd data-viz
   cp -r 01-Top30DistrictsInOdisha 02-YourNewProject
   ```

2. **Clean up:**
   ```bash
   cd 02-YourNewProject
   rm -rf node_modules out .claude .agents
   ```

3. **Update package.json:**
   ```json
   {
     "name": "02-yournewproject",
     "description": "Your new visualization"
   }
   ```

4. **Install and start:**
   ```bash
   npm install
   npm start
   ```

### Method 2: Create from Scratch

1. **Create new folder:**
   ```bash
   cd data-viz
   mkdir 02-YourNewProject
   cd 02-YourNewProject
   ```

2. **Initialize Remotion:**
   ```bash
   npm init -y
   npm install remotion react react-dom
   npm install -D @types/react @types/react-dom typescript
   ```

3. **Copy structure from project 01**

---

## 🔧 Git Workflow

### Initial Commit

```bash
cd data-viz

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Add Odisha districts visualization project"

# Check status
git status
```

### Adding Remote Repository (GitHub/GitLab)

```bash
# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/data-viz.git

# Push to remote
git push -u origin main
```

### Working with Projects

```bash
# Make changes in any project
cd 01-Top30DistrictsInOdisha
# ... edit files ...

# Go back to root to commit
cd ..

# Stage changes
git add 01-Top30DistrictsInOdisha/

# Commit
git commit -m "Update Odisha project: improve colors"

# Push
git push
```

---

## 📋 What Gets Committed

### ✅ Included in Git:
- Source code (`src/`)
- Data files (`public/*.csv`)
- Configuration files (`package.json`, `tsconfig.json`, etc.)
- Documentation (`README.md`, `SETUP_*.md`)
- Render scripts (`render.sh`, `render.bat`)

### ❌ Excluded from Git (.gitignore):
- `node_modules/` - Dependencies (too large)
- `out/` - Rendered videos (can be regenerated)
- `.remotion/` - Remotion cache
- `.claude/`, `.agents/` - Claude Code settings
- `.DS_Store`, `Thumbs.db` - OS files
- `*.log` - Log files

---

## 🎨 Repository Features

### 1. **Monorepo Structure**
- Multiple projects in one repository
- Shared git history
- Easy to manage related projects

### 2. **Independent Projects**
- Each project has its own dependencies
- Can use different versions of libraries
- Self-contained and portable

### 3. **Consistent Structure**
- All projects follow the same layout
- Easy to understand and navigate
- Standardized documentation

### 4. **Scalable**
- Add unlimited projects
- No interference between projects
- Clean separation of concerns

---

## 📊 Example: Multiple Projects

```
data-viz/
├── README.md
├── .gitignore
│
├── 01-Top30DistrictsInOdisha/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── 02-StateGDPVisualization/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── 03-ElectionResults2024/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── 04-CovidTrendsAnalysis/
    ├── src/
    ├── public/
    └── package.json
```

Each project is independent but shares the same git repository.

---

## 🛠️ Common Operations

### Clone the Repository
```bash
git clone <your-repo-url>
cd data-viz
```

### Work on a Specific Project
```bash
cd 01-Top30DistrictsInOdisha
npm install
npm start
```

### Update a Project
```bash
# Make changes in the project
cd 01-Top30DistrictsInOdisha
# ... edit files ...

# Commit from root
cd ..
git add .
git commit -m "Description of changes"
git push
```

### Create a New Project
```bash
cd data-viz
mkdir 02-NewProject
cd 02-NewProject
# ... set up project ...

# Commit from root
cd ..
git add 02-NewProject/
git commit -m "Add new project: NewProject"
git push
```

---

## 📦 Sharing Projects

### Share Entire Repository
```bash
git clone <repo-url>
cd data-viz
cd 01-Top30DistrictsInOdisha
npm install
npm start
```

### Share Single Project
```bash
# Export single project
cd data-viz
zip -r 01-Top30DistrictsInOdisha.zip 01-Top30DistrictsInOdisha/ \
  -x "*/node_modules/*" "*/out/*" "*/.claude/*"

# Recipient extracts and runs
unzip 01-Top30DistrictsInOdisha.zip
cd 01-Top30DistrictsInOdisha
npm install
npm start
```

---

## 💡 Best Practices

1. ✅ **Commit regularly** - Small, focused commits
2. ✅ **Write clear commit messages** - Describe what and why
3. ✅ **One project per folder** - Keep projects isolated
4. ✅ **Update main README** - When adding new projects
5. ✅ **Don't commit videos** - They're large and regenerable
6. ✅ **Document each project** - README in every project folder
7. ✅ **Use consistent naming** - Follow XX-ProjectName pattern

---

## 🎯 Quick Reference

```bash
# Navigate to repository root
cd data-viz

# Check status
git status

# View project list
ls -l

# Go to a project
cd 01-Top30DistrictsInOdisha

# Return to root
cd ..

# Commit changes
git add .
git commit -m "Your message"
git push
```

---

## 📞 Need Help?

- **Git Basics**: https://git-scm.com/book/en/v2
- **Monorepo Guide**: https://monorepo.tools/
- **GitHub**: https://docs.github.com/

---

**🎉 Your repository is ready! Start creating amazing visualizations!**
