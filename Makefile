build-cron-image:
	docker build -t cron-image -f Dockerfile-cron .

create-cron-job:
	kubectl create -f ./cronjob.yaml

delete-cron-job:
	kubectl delete cronjob cron-job