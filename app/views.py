from flask import render_template
from app import app
from .requests import get_quote

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quote=get_quote()
    blog_posts=Post.query.order_by(Post.posted.desc())
    author = Admin.query.first()
    return render_template('index.html', quote=quote, posts=blog_posts, author=author)

@app.route('/user',methods = ['GET','POST'])
@login_required
def admin(): 
    form=PostForm()
    quote=get_quote()        
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        category = form.category.data
        
        # Updated post instance
        this_post = Post(title=title, text=text, category=category, post_pic_path='photos/sample-image.jpeg')

        # save post method
        this_post.save_post()

        mail_list=[]
        subscribers=Subscriber.query.order_by(Subscriber.id.desc())
        for sub in subscribers:
            mail_list.append(sub.email)
        
        mail_message("New post on codescripts","email/new_post",mail_list,this_post=this_post)

        return redirect(url_for('.index'))
      
    title = 'New Post'

    return render_template('user.html', title=title, post_form=form, quote=quote)




