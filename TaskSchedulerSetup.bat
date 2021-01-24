rem https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/
rem https://www.windowscentral.com/how-create-task-using-task-scheduler-command-prompt
rem https://devblogs.microsoft.com/scripting/use-powershell-to-create-scheduled-tasks/

rem schtasks /create /sc daily /tn "runImageGetter" /tr "runImageGetter.bat" /st 15:00
rem                                                      ^Full Path!!! & other settings

$action = New-ScheduledTaskAction -Execute "path_to_batch_object.bat"
$trigger = New-ScheduledTaskTrigger -Daily -At 3pm
$principal = "" rem do I need this? has to be run as background process!
$settings = New-ScheduledTaskSettingsSet

$data = New-ScheduledTask -Action $action -Principal $principal -Trigger $trigger -Settings $settings

Register-ScheduledTask runImageGetter -InputObject $data
