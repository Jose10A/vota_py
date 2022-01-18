from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = "email/activation.html"


class ConfirmationEmail(email.ActivationEmail):
    template_name = "email/confirmation.html"


class PasswordResetEmail(email.ActivationEmail):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        return context


class PasswordChangedConfirmationEmail(email.ActivationEmail):
    template_name = "email/password_changed_confirmation.html"


class UsernameChangedConfirmationEmail(email.ActivationEmail):
    template_name = "email/username_changed_confirmation.html"


class UsernameResetEmail(email.ActivationEmail):
    template_name = "email/username_reset.html"
