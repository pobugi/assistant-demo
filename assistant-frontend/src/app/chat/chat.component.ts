import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
})
export class ChatComponent {
  userInput: string = '';
  messages: { sender: string; content: string }[] = [];

  constructor(private http: HttpClient) {
  }

  sendMessage() {
    if (!this.userInput.trim()) return;

    // Add the user message
    this.messages.push({sender: 'user', content: this.userInput});

    // Send the message to the backend
    this.http
      .post<{ response: string }>('http://127.0.0.1:8000/query', {
        user_input: this.userInput,
      })
      .subscribe(
        (response) => {
          // Add the assistant response
          this.messages.push({sender: 'assistant', content: response.response});
        },
        (error) => {
          console.error('Error:', error);
          this.messages.push({sender: 'assistant', content: 'Something went wrong. Please try again.'});
        }
      );

    // Clear the input field
    this.userInput = '';
  }
}
