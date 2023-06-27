import graphene
from graphene_django import DjangoObjectType
from main.models import Category, Post

# тут классы наз-ся представлениями


# работает как serializers
class CategoryModelType(DjangoObjectType):
    class Meta:
        model = Category


class PostModelType(DjangoObjectType):
    class Meta:
        model = Post


# работает как Viewset
class Query(graphene.ObjectType):
    category_model = graphene.List(CategoryModelType)
    post_model = graphene.List(PostModelType)

    def resolve_category_model(self, info):
        return Category.objects.all()
    
    def resolve_post_model(self, info):
        return Post.objects.all()
    

# POST запрос
class CreateCategory(graphene.Mutation):       
    class Arguments:
        newname = graphene.String(required=True)

    category = graphene.Field(CategoryModelType)

    def mutate(self, info, newname):
        category = Category.objects.create(name=newname)
        return CreateCategory(category=category)


# PUT запрос
class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        newname = graphene.String()

    category = graphene.Field(CategoryModelType)  # экз сериалайзера для сравнения 

    def mutate(self, info, id, newname):
        category = Category.objects.get(id=id)
        if newname:
            category.name = newname
        category.save()
        return UpdateCategory(category=category)
    

# DELETE запрос
class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()  # False

    def mutate(self, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteCategory(success=True)


# GET запрос встроен в qraphQL


# Теперь создаем для модели Post:

# POST запрос
class CreatePost(graphene.Mutation):       
    class Arguments:
        newimage = graphene.String(required=True)
        newtitle = graphene.String(required=True)
        newdescription = graphene.String(required=True)
        category_id = graphene.Int(required=True)
        newlocation = graphene.String(required=True)


    post = graphene.Field(PostModelType)

    def mutate(self, info, newimage, newtitle, newdescription, newlocation, category):
        post = Post.objects.create(image=newimage, title=newtitle, description=newdescription, location=newlocation, category=Category.objects.get(id=category))
        return CreatePost(post=post)
    

# PUT запрос
class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        newimage = graphene.String()
        newtitle = graphene.String()
        newdescription = graphene.String()
        category_id = graphene.Int()
        newlocation = graphene.String()
        

    post = graphene.Field(PostModelType)  # экз сериалайзера для сравнения 

    def mutate(self, info, id, newimage, newtitle, newdescription, newlocation, category_id):
        post = Post.objects.get(id=id)
        if newimage:
            post.image = newimage
        if newtitle:
            post.title = newtitle
        if newdescription:
            post.description = newdescription
        if newlocation:
            post.location = newlocation
        # if category_id:
        #     post.category = Category.objects.get(id=category_id)

        post.save()
        return UpdatePost(post=post)
    

# DELETE запрос
class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()  # False

    def mutate(self, info, id):
        post = Post.objects.get(id=id)
        post.delete()
        return DeletePost(success=True)
    


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()



# работает как routers / регистрируем тут
schema = graphene.Schema(query=Query, mutation=Mutation)
