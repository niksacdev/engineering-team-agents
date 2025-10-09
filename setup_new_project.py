#!/usr/bin/env python3
"""
Engineering Team Agents - New Project Setup Script

This script copies the engineering team agents structure to a new project,
creating all necessary folders and files for collaborative AI development.

Usage:
    python setup_new_project.py <folder_path>

Examples:
    python setup_new_project.py my_new_project
    python setup_new_project.py projects/my_new_project
    python setup_new_project.py /path/to/my_new_project
    python setup_new_project.py C:\\Projects\\my_new_project
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from typing import List, Tuple


class ProjectSetup:
    """Handles the setup of a new project with engineering team agents."""
    
    def __init__(self, source_dir: Path):
        self.source_dir = source_dir
        self.files_to_copy = [
            'AGENTS.md',
            'CONTRIBUTING.md',
            'LICENSE'
        ]
        self.directories_to_copy = [
            '.github',
            '.claude', 
            'docs'
        ]
        self.optional_files = [
            'README.md'  # Optional because projects might have their own
        ]
    
    def validate_source_directory(self) -> bool:
        """Validate that the source directory contains expected engineering team agents structure."""
        required_items = ['AGENTS.md', '.github', 'docs']
        
        for item in required_items:
            item_path = self.source_dir / item
            if not item_path.exists():
                print(f"❌ Error: Required item '{item}' not found in source directory")
                print(f"   Expected path: {item_path}")
                return False
        
        return True
    
    def create_target_directory(self, target_path: Path) -> bool:
        """Create the target directory if it doesn't exist."""
        try:
            target_path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"❌ Error creating target directory: {e}")
            return False
    
    def copy_file(self, source_file: Path, target_file: Path) -> bool:
        """Copy a single file with error handling."""
        try:
            # Create parent directories if they don't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, target_file)
            return True
        except Exception as e:
            print(f"❌ Error copying {source_file} to {target_file}: {e}")
            return False
    
    def copy_directory(self, source_dir: Path, target_dir: Path) -> bool:
        """Copy a directory recursively with error handling."""
        try:
            if target_dir.exists():
                shutil.rmtree(target_dir)
            shutil.copytree(source_dir, target_dir)
            return True
        except Exception as e:
            print(f"❌ Error copying directory {source_dir} to {target_dir}: {e}")
            return False
    
    def create_project_structure(self, target_path: Path) -> Tuple[int, int]:
        """Create the complete project structure in the target directory."""
        success_count = 0
        error_count = 0
        
        print(f"📁 Setting up engineering team agents in: {target_path}")
        print()
        
        # Copy required files
        print("📄 Copying core files...")
        for filename in self.files_to_copy:
            source_file = self.source_dir / filename
            target_file = target_path / filename
            
            if source_file.exists():
                if self.copy_file(source_file, target_file):
                    print(f"   ✅ {filename}")
                    success_count += 1
                else:
                    error_count += 1
            else:
                print(f"   ⚠️  {filename} (not found in source)")
        
        # Copy optional files
        print("\n📄 Copying optional files...")
        for filename in self.optional_files:
            source_file = self.source_dir / filename
            target_file = target_path / filename
            
            if source_file.exists() and not target_file.exists():
                if self.copy_file(source_file, target_file):
                    print(f"   ✅ {filename}")
                    success_count += 1
                else:
                    error_count += 1
            elif target_file.exists():
                print(f"   ⏭️  {filename} (already exists, skipping)")
            else:
                print(f"   ⚠️  {filename} (not found in source)")
        
        # Copy directories
        print("\n📁 Copying agent directories...")
        for dirname in self.directories_to_copy:
            source_dir = self.source_dir / dirname
            target_dir = target_path / dirname
            
            if source_dir.exists():
                if self.copy_directory(source_dir, target_dir):
                    print(f"   ✅ {dirname}/")
                    success_count += 1
                else:
                    error_count += 1
            else:
                print(f"   ⚠️  {dirname}/ (not found in source)")
        
        # Create additional project directories
        print("\n📁 Creating project workspace directories...")
        project_dirs = [
            'src',
            'tests',
            'docs/product',
            'docs/architecture', 
            'docs/code-review',
            'docs/ux',
            'docs/responsible-ai',
            'docs/gitops'
        ]
        
        for dir_path in project_dirs:
            full_path = target_path / dir_path
            try:
                full_path.mkdir(parents=True, exist_ok=True)
                print(f"   ✅ {dir_path}/")
                success_count += 1
            except Exception as e:
                print(f"   ❌ {dir_path}/ - Error: {e}")
                error_count += 1
        
        return success_count, error_count
    
    def create_project_readme(self, target_path: Path, project_name: str) -> bool:
        """Create a basic README if one doesn't exist."""
        readme_path = target_path / 'README.md'
        
        if readme_path.exists():
            return True
        
        readme_content = f"""# {project_name}

## Engineering Team Agents Setup

This project includes collaborative AI engineering agents for:
- 🏗️  **Architecture Review** - System design and technical decisions
- 🔍 **Code Quality** - Security-first code review and quality validation  
- 📋 **Product Management** - Requirements clarification and business value
- 🎨 **UX Design** - User journey mapping and accessibility validation
- 🤖 **Responsible AI** - Bias prevention and ethical AI development
- 🚀 **DevOps** - CI/CD optimization and deployment automation

## Quick Start

### GitHub Copilot Users
Use chatmode commands for collaborative development:
- `/architecture-review` - Validate system design decisions
- `/code-quality` - Review code for security and quality
- `/pm-requirements` - Clarify business requirements
- `/ui-validation` - Validate user experience design
- `/responsible-ai` - Ensure ethical AI development
- `/cicd-optimization` - Optimize deployment processes

### Claude Users  
Access specialized agents in the `.claude/agents/` directory for expert guidance.

## Development Workflow

1. **Requirements First**: Start with `/pm-requirements` to clarify user needs
2. **Design Review**: Use `/architecture-review` for technical decisions
3. **Implementation**: Follow `/code-quality` guidance for secure, maintainable code
4. **User Experience**: Validate with `/ui-validation` for user-facing features
5. **Deployment**: Optimize with `/cicd-optimization` for reliable releases

## Documentation

All agent interactions create persistent documentation in:
- `docs/product/` - Requirements and user stories
- `docs/architecture/` - Architecture Decision Records (ADRs)
- `docs/code-review/` - Code review reports
- `docs/ux/` - User journey maps and accessibility reports
- `docs/responsible-ai/` - Responsible AI documentation
- `docs/gitops/` - Deployment guides and operational runbooks

---

*Generated by Engineering Team Agents setup script*
"""
        
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            return True
        except Exception as e:
            print(f"❌ Error creating README.md: {e}")
            return False
    
    def setup_project(self, target_path_str: str) -> bool:
        """Main setup method that orchestrates the entire process."""
        # Convert to Path object and resolve
        target_path = Path(target_path_str).resolve()
        project_name = target_path.name
        
        print(f"🚀 Engineering Team Agents - New Project Setup")
        print(f"Source: {self.source_dir}")
        print(f"Target: {target_path}")
        print(f"Project: {project_name}")
        print("=" * 60)
        
        # Validate source directory
        if not self.validate_source_directory():
            return False
        
        # Create target directory
        if not self.create_target_directory(target_path):
            return False
        
        # Check if target directory is empty (or only contains common files)
        existing_files = list(target_path.glob('*'))
        if existing_files:
            print(f"⚠️  Target directory is not empty ({len(existing_files)} items found)")
            response = input("Continue anyway? (y/N): ").lower().strip()
            if response not in ['y', 'yes']:
                print("❌ Setup cancelled by user")
                return False
        
        # Copy project structure
        success_count, error_count = self.create_project_structure(target_path)
        
        # Create project README if needed
        print("\n📄 Creating project README...")
        if self.create_project_readme(target_path, project_name):
            print("   ✅ README.md created")
            success_count += 1
        else:
            error_count += 1
        
        # Summary
        print("\n" + "=" * 60)
        print(f"✅ Setup completed!")
        print(f"   Successfully processed: {success_count} items")
        if error_count > 0:
            print(f"   Errors encountered: {error_count} items")
        
        print(f"\n🎯 Next steps:")
        print(f"   1. cd {target_path}")
        print(f"   2. Initialize your git repository: git init")
        print(f"   3. Start using agent chatmodes for collaborative development!")
        print(f"\n📚 Documentation: {target_path / 'docs'}")
        print(f"🤖 GitHub Copilot Agents: {target_path / '.github' / 'chatmodes'}")
        print(f"🧠 Claude Agents: {target_path / '.claude' / 'agents'}")
        
        return error_count == 0


def main():
    """Main entry point for the setup script."""
    parser = argparse.ArgumentParser(
        description="Set up a new project with Engineering Team Agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python setup_new_project.py my_new_project
    python setup_new_project.py projects/my_new_project  
    python setup_new_project.py /path/to/my_new_project
    python setup_new_project.py C:\\Projects\\my_new_project
        """
    )
    
    parser.add_argument(
        'target_path',
        help='Path where the new project should be created'
    )
    
    parser.add_argument(
        '--source',
        help='Source directory containing engineering team agents (default: current directory)',
        default=None
    )
    
    if len(sys.argv) < 2:
        parser.print_help()
        return 1
    
    args = parser.parse_args()
    
    # Determine source directory
    if args.source:
        source_dir = Path(args.source).resolve()
    else:
        # Assume script is in the engineering-team-agents directory
        source_dir = Path(__file__).parent.resolve()
    
    if not source_dir.exists():
        print(f"❌ Error: Source directory does not exist: {source_dir}")
        return 1
    
    # Set up the project
    setup = ProjectSetup(source_dir)
    
    try:
        success = setup.setup_project(args.target_path)
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n❌ Setup cancelled by user")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())