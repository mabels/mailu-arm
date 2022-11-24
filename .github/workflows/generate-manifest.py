#!/usr/bin/env python3
import argparse
import yaml

def generate_manifest(image, tag, src_tag):
    return {
            "image": f"{image}:{tag}",
            "manifests": [
                {
                    "image": f"{image}:{src_tag}_aarch64",
                    "platform": {
                        "architecture": "arm64",
                        "os": "linux",
                        "variant": "v8"
                    }
                },
                {
                    "image": f"{image}:{src_tag}_x86_64",
                    "platform": {
                        "architecture": "amd64",
                        "os": "linux"
                    }
                }
            ]
    }

parser = argparse.ArgumentParser(prog = 'generate-manifest', description = 'generate a manifest')

parser.add_argument('--image')
parser.add_argument('--tag')
parser.add_argument('--src_tag')

args = parser.parse_args()
print(yaml.dump(generate_manifest(image=args.image, tag=args.tag, src_tag=args.src_tag)))
