from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class RegisterForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(), Email(message='请输入合法的email地址')])
    password = PasswordField('密码',validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

class UserEditProfileForm(FlaskForm):
    username = StringField(' 姓名',validators=[Required(), Length(3, 24, message='length between 3 and 24')])
    email = StringField('邮箱',validators=[Required(), Email(message='请输入合法的email地址')])
    password = PasswordField('密码',validators=[Required(), Length(6, 24)])
    phone = StringField('手机号', validators=[Required(), Length(11,11)])
    year = StringField('工作年限')
    resume = StringField('简历')
    submit = SubmitField('提交')
