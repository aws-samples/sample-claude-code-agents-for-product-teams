// Initial status file. Agents update this via update_status.py as artifacts are produced.
// Each key under "items" is "<phase-slug>/<kind>/<filename>", e.g. "5-build/artifacts/mvp.md".
// Valid status values: complete, in-progress, prepared, blocked, deferred, not-started.
window.PDLC_STATUS = {
  "project": {
    "name": "__PROJECT_NAME__",
    "path": "__PROJECT_PATH__",
    "started": "__STARTED_AT__"
  },
  "updated": "__STARTED_AT__",
  "items": {}
};
