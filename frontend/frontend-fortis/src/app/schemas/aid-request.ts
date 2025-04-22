export class AidRequest {
  id: number;
  name: string;
  description: string;
  image_path: string;
  deadline: Date;
  location: string;
  status: string;
  image!: string;
  soldier_id: number;
  volunteer_id: number;
  category_id: number;

  constructor(
    id: number,
    name: string,
    description: string,
    image_path: string,
    deadline: Date,
    location: string,
    status: string,
    image: string, 
    soldier_id: number,
    volunteer_id: number,
    category_id: number
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.image_path = image_path;
    this.deadline = deadline;
    this.location = location;
    this.status = status;
    this.image = image;
    this.soldier_id = soldier_id;
    this.volunteer_id = volunteer_id;
    this.category_id = category_id;
  }
}
