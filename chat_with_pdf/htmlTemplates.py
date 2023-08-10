css = '''
<style>

.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
   <p>bot</p>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
       <p>user</p>
    <div class="message">{{MSG}}</div>
</div>
'''