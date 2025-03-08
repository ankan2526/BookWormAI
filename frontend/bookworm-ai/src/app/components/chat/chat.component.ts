import { NgClass, NgFor, NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-chat',
  imports: [NgFor, NgIf, NgClass, FormsModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})

export class ChatComponent {
  messages: { text: string, sender: 'user' | 'ai' }[] = [];
  userInput: string = '';

  sendMessage() {
    if (this.userInput.trim()) {
      this.messages.push({ text: this.userInput, sender: 'user' });

      // Simulate AI response after a short delay
      setTimeout(() => {
        this.messages.push({ text: 'This is an AI response.', sender: 'ai' });
      }, 1000);

      this.userInput = '';
    }
  }
}
