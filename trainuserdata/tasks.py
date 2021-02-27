from celery import shared_task

@shared_task
def shared_train(model,x_train, y_train):
    model.fit(x_train, y_train)
    return model
