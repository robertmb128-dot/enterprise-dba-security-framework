Write-Host "Starting Enterprise DBRE Security Deployment"

$python = "python"
$modulePath = "..\python-tools\permission_drift_detector"

Write-Host "Running permission and login drift detection"
& $python "$modulePath\permission_drift_detector.py"

if ($LASTEXITCODE -ne 0) {
    Write-Error "Security drift detection failed"
    exit 1
}

Write-Host "Security deployment completed (detection-only)"

