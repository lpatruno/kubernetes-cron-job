from os import path
import yaml
from kubernetes import client, config


def main():
    # Load kubernetes config available from within Pods
    config.load_incluster_config()

    # Create job
    with open(path.join(path.dirname(__file__), "job.yaml")) as f:
        dep = yaml.load(f)
        print("TODO: Change the job name here")
        k8s_beta = client.BatchV1Api()
        resp = k8s_beta.create_namespaced_job(
            body=dep, namespace="default")
        print("Job created. status='%s'" % str(resp.status))


if __name__ == '__main__':
    main()