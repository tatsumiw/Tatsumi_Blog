#encoding: utf-8
from flask import Flask,render_template,request,redirect,url_for,session,make_response
import config
import os
import datetime
import random
from exts import db
from functools import wraps
from sqlalchemy import or_
from models import Article,Commenary,Dynamic #导入数据库模型

app = Flask(__name__)
app.config.from_object(config)   #导入config文件的相关参数
db.init_app(app)                 #初始化db

#登录限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

#个人主页
@app.route('/personal/')
def personal():
    return render_template('personal.html')

#浏览首页(添加了分页功能)
@app.route('/',methods =['GET','POST'])
def index():
    page = request.args.get('page',1,type=int)
    if Article.query.order_by('-read_times').first():
        context = {
            'pagination':Article.query.order_by('-create_time').paginate(page,
                        per_page = 5,error_out= False),
            'articles':Article.query.order_by('-create_time').paginate(page,
                        per_page = 5,error_out= False).items,
            'num_article': Article.query.filter(Article.label==u'文章').count(),
            'num_project': Article.query.filter(Article.label==u'项目').count(),
            'num_life': Article.query.filter(Article.label==u'生活').count(),
            'num_2017': Article.query.filter(Article.create_time >= '2017-01-01').filter(
                Article.create_time <= '2017-12-31').count(),
            'num_2018': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').count(),
            'num_read': Article.query.order_by('-read_times')[0:5],
            'activity':Dynamic.query.order_by('-id').first().content
        }
        return render_template('index.html',**context)
    else:
        return render_template('zero_index.html')

#浏览文章页
@app.route('/article/')
def article():
    page = request.args.get('page', 1, type=int)
    if Article.query.order_by('-read_times').first():
        context = {
            'pagination': Article.query.filter(Article.label==u'文章').order_by('-create_time').
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.label==u'文章').order_by('-create_time').
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == u'文章').count(),
            'num_project': Article.query.filter(Article.label == u'项目').count(),
            'num_life': Article.query.filter(Article.label == u'生活').count(),
            'num_2017': Article.query.filter(Article.create_time >= '2017-01-01').filter(
                Article.create_time <= '2017-12-31').count(),
            'num_2018': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').count(),
            'num_read': Article.query.order_by('-read_times')[0:5],
            'activity': Dynamic.query.order_by('-id').first().content
        }
        return render_template('front_article.html',**context)
    else:
        return render_template('zero_index.html')

#浏览项目页
@app.route('/projects/')
def projects():
    page = request.args.get('page', 1, type=int)
    if Article.query.order_by('-read_times').first():
        context = {
            'pagination': Article.query.filter(Article.label==u'项目').order_by('-create_time').
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.label==u'项目').order_by('-create_time').
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == u'文章').count(),
            'num_project': Article.query.filter(Article.label == u'项目').count(),
            'num_life': Article.query.filter(Article.label == u'生活').count(),
            'num_2017': Article.query.filter(Article.create_time >= '2017-01-01').filter(
                Article.create_time <= '2017-12-31').count(),
            'num_2018': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').count(),
            'num_read': Article.query.order_by('-read_times')[0:5],
            'activity': Dynamic.query.order_by('-id').first().content
        }
        return render_template('front_projects.html',**context)
    else:
        return render_template('zero_index.html')

#浏览生活页
@app.route('/life/')
def life():
    page = request.args.get('page', 1, type=int)
    if Article.query.order_by('-read_times').first():
        context = {
            'pagination': Article.query.filter(Article.label==u'生活').order_by('-create_time').
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.label==u'生活').order_by('-create_time').
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == u'文章').count(),
            'num_project': Article.query.filter(Article.label == u'项目').count(),
            'num_life': Article.query.filter(Article.label == u'生活').count(),
            'num_2017': Article.query.filter(Article.create_time >= '2017-01-01').filter(
                Article.create_time <= '2017-12-31').count(),
            'num_2018': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').count(),
            'num_read': Article.query.order_by('-read_times')[0:5],
            'activity': Dynamic.query.order_by('-id').first().content
        }
        return render_template('front_life.html',**context)
    else:
        return render_template('zero_index.html')

# 2017归档页
@app.route('/2017/')
def year2017():
    page = request.args.get('page', 1, type=int)
    if Article.query.order_by('-read_times').first():
        context = {
            'pagination': Article.query.filter(Article.create_time>='2017-01-01').filter(Article.create_time <= '2017-12-31').order_by('-create_time').
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.create_time>='2017-01-01').filter(Article.create_time <= '2017-12-31').order_by('-create_time').
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == u'文章').count(),
            'num_project': Article.query.filter(Article.label == u'项目').count(),
            'num_life': Article.query.filter(Article.label == u'生活').count(),
            'num_2017': Article.query.filter(Article.create_time>='2017-01-01').filter(Article.create_time <= '2017-12-31').count(),
            'num_2018': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').count(),
            'num_read': Article.query.order_by('-read_times')[0:5],
            'activity': Dynamic.query.order_by('-id').first().content
        }
        return render_template('front_2017.html',**context)
    else:
        return render_template('zero_index.html')

# 2018归档页
@app.route('/2018/')
def year2018():
    page = request.args.get('page', 1, type=int)
    if Article.query.order_by('-read_times').first():
        context = {
            'pagination': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').order_by('-create_time').
                paginate(page, per_page=5, error_out=False),
            'articles': Article.query.filter(Article.create_time >= '2018-01-01').filter(
                Article.create_time <= '2018-12-31').order_by('-create_time').
                paginate(page, per_page=5, error_out=False).items,
            'num_article': Article.query.filter(Article.label == u'文章').count(),
            'num_project': Article.query.filter(Article.label == u'项目').count(),
            'num_life': Article.query.filter(Article.label == u'生活').count(),
            'num_2017': Article.query.filter(Article.create_time >= '2017-01-01').filter(
                Article.create_time <= '2017-12-31').count(),
            'num_2018': Article.query.filter(Article.create_time>='2018-01-01').filter(Article.create_time <= '2018-12-31').count(),
            'num_read': Article.query.order_by('-read_times')[0:5],
            'activity': Dynamic.query.order_by('-id').first().content
        }
        return render_template('front_2018.html', **context)
    else:
        return render_template('zero_index.html')

#文章详细页
@app.route('/detail/<articel_id>')
def detail(articel_id):
    #游客每次点击阅读原文，阅读数加1
    if session.get('user_id') != 1:
        article1 = Article.query.filter(Article.id == articel_id).first()
        article1.read_times = article1.read_times + 1
        db.session.commit()
    #获取要渲染的变量数据
    context = {
    'article_model' : Article.query.filter(Article.id == articel_id).first(),
    'num_article' : Article.query.filter(Article.label == u'文章').count(),
    'num_project' :  Article.query.filter(Article.label == u'项目').count(),
    'num_life' : Article.query.filter(Article.label == u'生活').count(),
        'num_2017': Article.query.filter(Article.create_time >= '2017-01-01').filter(
            Article.create_time <= '2017-12-31').count(),
        'num_2018': Article.query.filter(Article.create_time >= '2018-01-01').filter(
            Article.create_time <= '2018-12-31').count(),
    'num_read': Article.query.order_by('-read_times')[0:5],
    'activity': Dynamic.query.order_by('-id').first().content
    }
    return render_template('detail.html',**context)




#评论功能
@app.route('/commentaries/',methods=['POST'])
def commentaries():
    content = request.form.get('commentary')
    if content :
        wenzhang_id = request.form.get('article_id')
        pinglun = Commenary(content = content,article_id = wenzhang_id)
        db.session.add(pinglun)
        db.session.commit()
        return redirect(url_for('detail',articel_id = wenzhang_id))
    else:
        return render_template('404.html',baocuo =u'评论不能为空，请检查后重新输入') #评论为空

#查找功能
@app.route('/search/')
def search():
    q = request.args.get('q')
    #标题或内容
    if Article.query.filter(or_(Article.title.contains(q),Article.content.contains(q))).first() :
        context = {
        'articles' : Article.query.filter(or_(Article.title.contains(q),Article.content.contains(q))).order_by('-create_time').all(),
        'num_article' : Article.query.filter(Article.label == u'文章').count(),
        'num_project' :  Article.query.filter(Article.label == u'项目').count(),
        'num_life' : Article.query.filter(Article.label == u'生活').count(),
        'num_read': Article.query.order_by('-read_times')[0:5]
        }
        return render_template('search.html',**context)
    else :
        return render_template('404.html',baocuo =u'搜索为空，请更换关键字后重试') #搜索为空


#登录(博主的账号密码信息已存在数据库中)
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usernum = request.form.get('usernum')
        password = request.form.get('password')
        #验证登录信息(账号密码保存在参数文件中)
        if usernum == config.USERNAME_LOGIN and password == config.PASSWORD_LOGIN:
            session['user_id'] = 1 #保存用户id信息
            #如果想31天内都不需要登录
            #session.permanent = True
            return redirect(url_for('back_index'))
        else:
            return u'账号或密码错误，请检查后重试'

#博主注销(退出登录状态)
@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index'))

#后台首页
@app.route('/back_index/',methods=['GET','POST'])
@login_required
def back_index():
        if request.method == 'GET':
            return render_template('back_index.html')
        else:
            content = request.form.get('content')
            dynamic = Dynamic(content=content)
            db.session.add(dynamic)
            db.session.commit()
            return redirect(url_for('back_index'))


#后台列表页
@app.route('/back_list/')
@login_required
def back_list():
    context = {
        'articles':Article.query.order_by('-create_time').all()
    }
    return render_template('back_list.html',**context)

#后台文章编辑页
@app.route('/back_edit/',methods=['GET','POST'])
@login_required
def back_edit():
    if request.method == 'GET':
        return render_template('back_edit.html')
    else:
        label = request.form.get('label')
        title = request.form.get('title')
        content = request.form.get('editor1')
        read_times = 0
        article = Article(label=label,title=title,content=content,read_times=read_times)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('back_index'))

# 后台文章编辑功能
@app.route('/back_update/<articel_id>', methods=['GET', 'POST'])
@login_required
def back_update(articel_id):
    article1 = Article.query.filter(Article.id == articel_id).first()
    if request.method == 'GET':
        return render_template('back_update.html', article1=article1)
    else:
        article1 = Article.query.filter(Article.id == articel_id).first()
        article1.label = request.form.get('label')
        article1.title = request.form.get('title')
        article1.content = request.form.get('editor1')
        article1.create_time = article1.create_time
        article1.update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article1.read_times = article1.read_times
        db.session.commit()
    return redirect(url_for('back_list'))

# 后台文章删除功能
@app.route('/back_drop/<articel_id>', methods=['GET','POST'])
@login_required
def back_drop(articel_id):
    while Commenary.query.filter(Commenary.article_id == articel_id).first():
        commentary1 = Commenary.query.filter(Commenary.article_id == articel_id).first()
        db.session.delete(commentary1) #首先删除文章对应的评论

    article1 = Article.query.filter(Article.id == articel_id).first()
    db.session.delete(article1)
    db.session.commit()                #载删除对应的文章
    return redirect(url_for('back_list'))

#文章图片上传命名函数
def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

#CKEditor富文本编辑器
@app.route('/ckupload/', methods=['POST', 'OPTIONS'])
def ckupload():
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")

    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)

        filepath = os.path.join(app.static_folder, 'upload', rnd_name)

        # 检查路径是否存在，不存在则创建
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'

        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
    else:
        error = 'post error'

    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)

    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response

#上下文处理器钩子函数(设置的是登录后显示用户名)
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')#如果存在user_id则已成功登录，返回用户名user：温毛
    if user_id:
        return {'user':u'温毛'}
    return {}

if __name__ == "__main__":
    app.run()
