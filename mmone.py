import argparse
import yaml
from includes.statusdroid import statusdroid
from includes.httpd_logs import httpd_logs
from includes.mmone import mmone


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        help="path to yaml configuration file file",
        action="store")
    args = parser.parse_args()

    if args.config:
        with open(args.config) as fl:
            config_dict = yaml.load(fl.read())
            st = statusdroid(
                config_dict['statusdroid_statuspage']
            )
            mu_remote = st.get_intensity_to_minute()
            hd = httpd_logs(
                config_dict['httpd_logs']
            )
            lambda_local = hd.get_hour_to_minute_count()

            m = mmone(mu_remote, lambda_local)
            print(m)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
