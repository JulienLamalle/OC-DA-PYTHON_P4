from controllers.scheduler import SchedulerController


class Main:
    def perform(self):
        scheduler = SchedulerController()
        scheduler.perform()


if __name__ == "__main__":
    main = Main()
    main.perform()
