print("-------------------------------------------------------------")
# The get() method on dicts and its "default" argument
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print("name_for_userid:", name_for_userid)
print("greeting(382):", greeting(382))
# "Hi Alice!"

print("greeting(333333):", greeting(333333))
# "Hi there!"
