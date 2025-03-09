import { NgClass, NgFor, NgIf } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MarkdownComponent, MarkdownModule } from 'ngx-markdown';

@Component({
  selector: 'app-chat',
  imports: [NgFor, NgIf, NgClass, FormsModule, MarkdownModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})

export class ChatComponent {
  messages: { text: string, sender: 'user' | 'ai' }[] = [];
  userInput: string = '';

  constructor(private http: HttpClient) {

  }

  sendMessage() {
    if (this.userInput.trim()) {
      this.messages.push({ text: this.userInput, sender: 'user' });

      // Simulate AI response after a short delay
      // setTimeout(() => {

      //   this.messages.push({ text: 'This is an AI response.', sender: 'ai' });
      // }, 1000);

      this.http.post("http://127.0.0.1:5000/llm/invoke", {"query": this.userInput}).subscribe((result: any) => {
        this.messages.push({text: result.result, sender: 'ai'});
      })

      this.userInput = '';
    }
  }
}
