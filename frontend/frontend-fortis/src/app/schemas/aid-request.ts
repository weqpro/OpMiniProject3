export class AidRequest{
  id: number;
  name: string;
  description: string;
  image_path: string;
  endDate: Date;
  location: string;
  status: string;
  soldier_id: number;
  volunteer_id: number;

  constructor(
    id: number,
    name: string,
    description: string,
    image_path: string,
    endDate: Date,
    location: string,
    status: string,
    soldier_id: number,
    volunteer_id: number,

  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.image_path = image_path;
    this.endDate = endDate;
    this.location = location;
    this.status = status;
    this.soldier_id = soldier_id;
    this.volunteer_id = volunteer_id
  }
}
