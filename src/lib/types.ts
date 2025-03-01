import type { Message } from 'ai';

export interface Chat extends Record<string, unknown> {
	id: string;
	title: string;
	createdAt: Date;
	userId: string;
	path: string;
	messages: Message[];
	sharePath?: string;
}
