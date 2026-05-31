"""Inspect the current Resolve project without mutating it."""

from __future__ import annotations

import sys

from _resolve_common import get_current_project


def safe_len(value: object) -> int:
    return len(value) if isinstance(value, list) else 0


def main() -> int:
    try:
        _resolve, _project_manager, project = get_current_project()
        if project is None:
            print("No project is currently open.")
            return 0

        print(f"Project: {project.GetName()}")
        timeline_count = project.GetTimelineCount()
        print(f"Timeline count: {timeline_count}")
        current_timeline = project.GetCurrentTimeline()
        print(f"Current timeline: {current_timeline.GetName() if current_timeline else '<none>'}")
        for index in range(1, timeline_count + 1):
            timeline = project.GetTimelineByIndex(index)
            if timeline is None:
                continue
            print(
                f"- Timeline {index}: {timeline.GetName()} "
                f"frames={timeline.GetStartFrame()}-{timeline.GetEndFrame()} "
                f"video_tracks={timeline.GetTrackCount('video')} "
                f"audio_tracks={timeline.GetTrackCount('audio')} "
                f"subtitle_tracks={timeline.GetTrackCount('subtitle')}"
            )

        media_pool = project.GetMediaPool()
        root = media_pool.GetRootFolder() if media_pool else None
        if root:
            print(f"Media Pool root: {root.GetName()}")
            print(f"Root clips: {safe_len(root.GetClipList())}")
            print(f"Root subfolders: {safe_len(root.GetSubFolderList())}")
        return 0
    except Exception as exc:
        print(f"Project inspection failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
