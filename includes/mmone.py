

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

    def e_time_to_serve_task(self):
        return (1 / self.mu)

    def e_time_of_wait_in_queue(self):
        return

    def __str__(self):
        return \
            "MU - intensity of serve per min - " + str(self.mu) + "\n" + \
            "LA - insensity of messages per min - " + str(self.la) + "\n" \
            "RHO - E occupacy per min - " + str(self.get_rho()) + "\n" \
            "System is " + (
                "stable" if self.get_rho() < 1 else "unstable"
            ) + "\n"
            # \
            # "E count of tasks in the queue " + str(
            #     self.e_count_task_in_queue()
            # ) + "\n"
