from tabulate import tabulate


class mmone:
    """ MM1 class for estimating basic equations. M suggests Poisson distribution.
    """
    def __init__(self, mu, la):
        self.mu = mu
        self.la = la

    def get_rho(self):
        self.rho = self.la / self.mu
        return self.rho

    def p_server_empty(self):
        return (
            1 / (1 + self.get_rho())
        )

    def p_new_task_wait():
        return

    def e_occupacy(self):
        return self.get_rho()

    def p_of_k_tasks_server(self, k):
        return (
            (self.get_rho() ** k) *
            self.p_server_empty()
        )

    def e_count_task_in_queue(self):
        return (
            self.p_of_k_tasks_server(1) *
            (
                self.get_rho() / ((1 - self.get_rho()) ** 2)
            )
        )

    def e_count_of_task_in_whole_system(self):
        return (
            self.e_count_task_in_queue() + self.e_occupacy()
        )

    def p_of_task_wait_for_server(self):
        return (
            self.p_of_k_tasks_server(1) *
            (
                1 / (1 - self.get_rho())
            )
        )

    def e_time_to_serve_task(self):
        return (1 / self.mu)

    def e_time_of_wait_in_queue(self):
        return (
            self.p_of_task_wait_for_server() / (
                1 * self.mu - self.la
            )
        )

    def e_time_of_task_in_whole_system(self):
        return (
            self.e_time_of_wait_in_queue() + self.e_time_to_serve_task()
        )

    def __str__(self):
        return \
            tabulate([
                ["Mu - intensity of serve per minute:", str(self.mu)],
                ["Lambda - insensity of messages per minute:", str(self.la)],
                ["Rho expected occupacy per minute:", str(self.get_rho())],
                ["System is:", "stable" if self.get_rho() < 1 else "unstable"],
                [
                    "Expected count of tasks in the queue:",
                    str(self.e_count_task_in_queue())
                ],
                [
                    "Expected count of tasks in system:",
                    str(self.e_count_of_task_in_whole_system())
                ],
                [
                    "Expected time to serve the task:",
                    str(self.e_time_to_serve_task())
                ],
                [
                    "Expected time to the task to wait in queue:",
                    str(self.e_time_of_wait_in_queue())
                ],
                [
                    "Expected time of task in whole system:",
                    str(self.e_time_of_task_in_whole_system())
                ]
            ], headers=['Description', 'Value'])
        # "MU - intensity of serve per min\t: " + str(self.mu) + "\n" + \
        # "LA - insensity of messages per min\t: " + str(self.la) + "\n" \
        # "RHO - E occupacy per min\t: " + str(self.get_rho()) + "\n" \
        # "System " + (
        #     "stable" if self.get_rho() < 1 else "unstable"
        # ) + "\n" \
        # "======== queue ========\n" \
        # "E count of tasks in the queue " + str(
        #     self.e_count_task_in_queue()
        # ) + "\n"
