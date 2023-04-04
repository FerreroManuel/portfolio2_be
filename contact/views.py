from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from rest_framework.response import Response
from rest_framework.views import APIView


class EmailAPI(APIView):

    def post(self, request):
        """
        Receives a POST request with the necesary information to create an email
        and send it to contact mail box
        """
        reqName = request.data.get('name')
        reqEmail = request.data.get('email')
        reqSubject = request.data.get('subject')
        if reqSubject == 'Otro':
            reqSubject = request.data.get('otherSubject')
        reqMessage = request.data.get('message')
        
        subject = f"Contacto desde la web: {reqSubject}"
        message = f"""
        \rDe: {reqName} <{reqEmail}>
        \rAsunto: {reqSubject}.
        \rMensaje:
        \r{reqMessage}
        """
        html_message = f"""
        <b>De:</b> {reqName} <i>&lt;{reqEmail}&gt;</i><br>
        <b>Asunto:</b> {reqSubject}.<br>
        <b>Mensaje:</b>
        <p>{reqMessage}</p>
        """

        mail = EmailMultiAlternatives(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_CONTACT_EMAIL],
            alternatives=[(html_message, "text/html")],
            reply_to=[reqEmail],
        )

        mail.send()

        return Response({'msg': 'Su mensaje ha sido envíado con éxito. Gracias por contactarse!'}, status=200)
