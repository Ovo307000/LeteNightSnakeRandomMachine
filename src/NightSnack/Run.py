from src.NightSnack import NightSnack, Tools, Setting

if __name__ == '__main__':
    print(f"NightSnack is running at {Setting.Config().get_config().get('configPath')}")
    print(f"Program version: {Setting.Config().get_config().get('version')}")

    NightSnack.print_statement()
    Tools.exit_wait()
