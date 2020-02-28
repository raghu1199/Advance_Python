class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement = engagement
        self.score = 0

    def __repr__(self):
        return f"<User {self.name}>"


def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement)
    except KeyError:
        print("Incorrect values Provided for calculation")
        raise
    else:
        if user.score > 500:
            send_engagement_notification(user)


def perform_calculation(metrices):
    return metrices['clicks'] * 5 + metrices['hits'] * 2


def send_engagement_notification(user):
    print(f"notification is sent to {user}")


my_user = User("Raghu", {'clicks': 61, 'hits': 100}) #try for key 'clik'

email_engaged_user(my_user)
