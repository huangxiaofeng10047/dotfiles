echo "======== start clean docker containers logs ========"
logs=$(find /var/lib/docker/containers/ -name *-json.log)
for log in $logs; do
	echo "clean containers logs : $log"
	cat /dev/null >$log
done
echo "======== end clean docker containers logs ========"
