export interface Review {
    id: number;
    review_text: string;
    rating: number;
    tags: string[];
    request_id: number;
    reported: boolean;
  }