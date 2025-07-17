from django.urls import path, include
from .views import user, openai, tiktok, lexcomia, usersettings, healthz, payment, account

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Test token
    path(r'home/', user.HomeView.as_view(), name='home'),

    # Registro
    path(r'register/', user.RegisterView.as_view(), name="register"),

    # Create token access and token refresh for uptade the token access
    path(r'token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path(r'token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    # Delete token access and add to the blacklist the token
    path(r'logout/', user.LogoutView.as_view(), name='logout'),

    # Update perfil
    path(r'update/', usersettings.UserDetailView.as_view(), name='settings'),

    # Endpoints for  OpenAI
    path(r'openai/<str:id>', openai.OpenAIApiView.as_view(
        {'get': 'recommend_video'}), name="recommend_video"),
    path(r'copy_ads/<str:id>',
         openai.OpenAIApiView.as_view({'get': 'recommend_copy'}), name="recommend_copy"),
    path(r'landing/<str:id>', openai.OpenAIApiView.as_view(
        {'get': 'recommend_landing'}), name="recommend_landing"),

    # Endpoint for TikTok Api
    path(r'tiktok/<str:id>', tiktok.TiktTokApiView.as_view(
        {'get': 'video_interest'}), name="video_interest"),

    # Endpoint for predictions Lexcom
    path(r'lexcom_five_class/', lexcomia.LexcomIA_ApiView.as_view(
        {'post': 'probability_percentage'}), name="probability_percentage"),

    # Endpoint for reset password
    path(r'password_reset/', include('django_rest_passwordreset.urls',
         namespace='password_reset')),

    # Endpoint for progress
    path(r'update_plan/', user.UpdateSearchPlanView.as_view(), name='update_plan'),
    path(r'user_info/', user.UserInfoView.as_view(), name='user_info'),
    path(r'increment_search_count/', user.IncrementSearchCountView.as_view(),
         name='increment_search_count'),


    # Endpoint for user pay
    path(r'get_email/', usersettings.UserEmailView.as_view(), name='get_email'),
    path(r'create_preference/', payment.PaymentApiView.as_view(
        {'post': 'create_preference'}), name="create_preference"),
    path(r'cache/', payment.CurrentPlan.as_view(
        {'post': 'cache'}), name="cache"),
    path(r'send_plan/', payment.CurrentPlan.as_view(
        {'post': 'send_plan'}), name="send_plan"),

    # Endpoint for test
    path(r'test/', healthz.TestView.as_view(), name='healthz'),

    # Endpoints for Login with Google
    # path(r'accounts/', include('allauth.urls')),
    # path(r'dj-rest-auth/', include('dj_rest_auth.urls')),
    # path(r'dj-rest-auth/registration/',
    #      include('dj_rest_auth.registration.urls')),
    path(r'dj-rest-auth/google/',
         account.GoogleLogin.as_view(), name="google_login"),
]
