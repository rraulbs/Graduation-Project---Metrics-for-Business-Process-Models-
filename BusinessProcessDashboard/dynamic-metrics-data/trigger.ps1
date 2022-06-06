$conf = Get-Content '.\env\conf.json' | ConvertFrom-Json
$path = "$PWD/logs/continuous-update-enabled.txt"
if($conf.keepUpdating -eq $true){
    if(![System.IO.File]::Exists($path)){
        New-Item -Path $path -ItemType File
    }
}
else{
    if([System.IO.File]::Exists($path)){
        Remove-Item -Path $path
    }
}