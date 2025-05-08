# rmKit_export

Export Manager for modular kit-based workflows in environment art for games.

## Overview

`rmKit_export` is a Blender add-on designed to streamline the export process for modular environment art assets in game development. It provides an intuitive interface for managing exportable objects, ensuring unique naming, and handling export paths dynamically. The add-on supports exporting objects to `.fbx` format and includes features like:

- Automatic synchronization of scene objects with the export manager.
- Dynamic export path generation based on scene and object properties.
- Support for batch exporting enabled objects.
- Customizable export settings via the Blender preferences panel.

## Features

- **Export Manager Panel**: A dedicated UI panel in the 3D View Sidebar for managing exportable objects.
- **Dynamic Path Management**: Export paths can be customized using placeholders like `$SceneDir`, `$SceneName`, and `$ObjectName`.
- **Batch Export**: Export multiple objects at once with the "Export Checked" feature.
- **Collision-Free Naming**: Ensures unique object names to avoid conflicts during export.
- **Integration with Blender's Dependency Graph**: Automatically updates the export manager when objects or scenes change.

## Installation

1. Download the repository as a `.zip` file.
2. In Blender, go to `Edit > Preferences > Add-ons`.
3. Click `Install...` and select the downloaded `.zip` file.
4. Enable the add-on by checking the box next to `rmKit_export`.

## Usage

1. Open the Export Manager panel in the 3D View Sidebar.
2. Add objects to the export list using the "Add" button.
3. Customize export paths in the add-on preferences.
4. Export individual objects or batch export enabled objects.

## Documentation

For detailed documentation, visit the [official documentation](https://rmkit.readthedocs.io/en/latest/).
