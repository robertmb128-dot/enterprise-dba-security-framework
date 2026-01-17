<#
Purpose:
Safely roll back security-related automation artifacts.
NO data loss.
NO permission removal by default.
#>

Write-Host "Starting rollback process..."

# Example: Disable scheduled jobs (not delete)
Get-ScheduledTask -TaskName "PermissionDrift*" -ErrorAction SilentlyContinue |
    Disable-ScheduledTask

# Example: Archive logs instead of deleting
$logPath = "C:\DBRE\logs"
$archivePath = "C:\DBRE\archive"

if (Test-Path $logPath) {
    New-Item -ItemType Directory -Force -Path $archivePath | Out-Null
    Move-Item "$logPath\*" $archivePath -Force
}

Write-Host "Rollback complete. No destructive actions performed."
