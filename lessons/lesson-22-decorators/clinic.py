from decorators import log_call, validate_appointment, timed, retry


@log_call
@timed
@validate_appointment
def confirm(appt):
    return appt


_seen = set()


@retry(attempts=3)
@log_call
def send_sms(appt):
    phone = appt["phone"]

    if phone.endswith("9") and phone not in _seen:
        _seen.add(phone)
        raise ConnectionError("gateway drop")

    return "sent:" + phone


def build_report(lines):
    confirmed = sum(line.startswith("ok ") for line in lines)
    skipped = sum(line.startswith("skip ") for line in lines)
    header = f"confirmed {confirmed}, skipped {skipped}"

    return "\n".join([header, *lines]) + "\n"
