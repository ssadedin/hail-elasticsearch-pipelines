#!/usr/bin/env python3

from kubernetes.shell_utils import simple_run as run

for genome_version, vcf_path in [
    ("37", "gs://seqr-reference-data/GRCh37/eigen/EIGEN_coding_noncoding.grch37.vds"),
    ("38", "gs://seqr-reference-data/GRCh38/eigen/EIGEN_coding_noncoding.liftover_grch38.vds"),
]:
    run(("python3 gcloud_dataproc/v02/run_script.py "
        "--cluster create-ht-mpc "
        "hail_scripts/v02/convert_vcf_to_hail.py "
        "--output-sites-only-ht "
        f"--genome-version {genome_version} "
        f"{vcf_path}"))
    