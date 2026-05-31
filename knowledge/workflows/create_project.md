# Create Project Workflow

## Purpose

Create a new Resolve project without overwriting existing projects or silently changing defaults.

## Applies To

- Resolve versions: 20.x, 21.x, user installed version to verify
- Edition: Free and Studio, cloud/collaboration features to verify
- OS: macOS, Windows, Linux
- Page: Project Manager
- Automation status: Scriptable after project API confirmation; cloud workflows need extra verification

## Required Inputs

- Project name.
- Project library or database context, if relevant.
- Initial frame rate, resolution, and color management only if the user wants non-default settings.
- Backup or template requirements, if any.

## Workflow

1. Check current project manager context.
2. Check whether a project with the target name exists.
3. Confirm any non-default settings before creation.
4. Create project through UI or confirmed `ProjectManager.CreateProject` workflow.
5. Open or inspect the created project.

## Risk Escalators

- Existing project name conflict.
- Cloud or collaborative project context.
- Changing default project settings.

## Verification

- Project exists with expected name.
- Project opens successfully.
- Initial settings match only the user-confirmed values.

## Source References

- Source ID: installed-developer-docs-user
- Source ID: bmd-product-overview-21
- Last verified: 2026-05-31
