# Script Environment Setup

## Applies To

- Resolve versions: installed Scripting README last updated 2025-10-07; user installed version to verify
- Edition: Verify Free/Studio scripting behavior in the user's environment
- OS: macOS, Windows, Linux
- Automation status: Confirmed for environment path patterns in installed Scripting README

## Purpose

Describe environment checks before running Resolve scripts.

## Preflight

- DaVinci Resolve must be running for external scripts.
- Python must be 64-bit and compatible with the installed scripting environment.
- External scripts may need `RESOLVE_SCRIPT_API`, `RESOLVE_SCRIPT_LIB`, and `PYTHONPATH`.
- Remote scripting access has security implications and should not be enabled casually.

## Common Module Paths

- macOS: `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules`
- Windows: `%PROGRAMDATA%\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules`
- Linux: `/opt/resolve/Developer/Scripting/Modules`

## Source References

- Source ID: installed-developer-docs-user
- Last verified: 2026-05-31
