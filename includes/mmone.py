

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
            self.p_of_k_tasks_server() *
            (
                self.get_rho() / ((1 - self.get_rho()) ** 2)
            )
        )

    def e_time_to_serve_task(self):
        return (1 / self.mu)

    def e_time_of_wait_in_queue(self):
        return
