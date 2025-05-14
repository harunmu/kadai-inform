from datetime import datetime


def check_deadline(class_name_list,kadai_deadline_list):

    email_contents = []
    current_day = datetime.now().date()

    for class_name, kadai_deadline in zip(class_name_list,kadai_deadline_list):
        deadline = datetime.strptime(kadai_deadline[0],'%Y/%m/%d')
        deadline_date = deadline.date()

        deadline_limit = deadline_date - current_day
        deadline_limit_date = deadline_limit.days
        if deadline_limit_date <= 7:
            contents_info = [deadline_limit_date,class_name,deadline_date]
            email_contents.append(contents_info)

    return email_contents