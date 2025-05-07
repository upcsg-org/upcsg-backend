from main.utils.generic_api import GenericView
from .models import Concern
from .serializers import ConcernSerializer, EmailFormSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from user.models import User

class TrackConcernView(GenericView):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ["list", "retrieve"]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ManageConcernView(GenericView):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    permission_classes = [IsAdminUser]

class EmailFormView(APIView):
    """
    API view to send suggestion emails to admin
    """
    
    def post(self, request, *args, **kwargs):
        serializer = EmailFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            content = serializer.validated_data['content']
            
            # Construct admin notification email
            subject = f"Suggestion from {name}"
            # Plain text fallback for admin
            plain_message = f"From: {name} ({email})\n\n{content}"
            
            # HTML version for admin using template
            context = {
                'name': name,
                'email': email,
                'content': content
            }
            html_message = render_to_string('emails/admin_notification.html', context)
            
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            
            # Notification for concern sender
            subject_sender = "Thank you for your suggestion"
            # Plain text fallback for sender
            plain_message_sender = f"Dear {name},\n\nThank you for your suggestion. We will review it and get back to you soon.\n\nBest regards,\nThe CSG Team"
            
            # HTML version for sender using template
            html_message_sender = render_to_string('emails/user_confirmation.html', context)
            
            from_email_sender = settings.DEFAULT_FROM_EMAIL
            recipient_list_sender = [email]
            
            try:
                # Create a new concern object
                Concern.objects.create(
                    name=name,
                    email=email,
                    content=content,
                )

                # Send email to admin
                send_mail(
                    subject, 
                    plain_message, 
                    from_email, 
                    recipient_list,
                    html_message=html_message
                )
                
                # Send confirmation email to user
                send_mail(
                    subject_sender, 
                    plain_message_sender, 
                    from_email_sender, 
                    recipient_list_sender,
                    html_message=html_message_sender
                )

                return Response(
                    {"message": "Your suggestion has been sent successfully!"},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {"error": f"Failed to send email: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
