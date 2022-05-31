import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { Router } from '@angular/router';
import { UserService } from '../user.service';


@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css'],
})
export class LogInComponent implements OnInit {
  user: User = new User();
  submitted = false;
 

  constructor(private userService: UserService, private router: Router) {}

  ngOnInit() {}
  newUser(): void {
    this.submitted = false;
    this.user = new User();
  }
  save() {
    this.userService.createUser(this.user).subscribe(
      (data: any) => {
        console.log('data', data), (this.user = new User());
        this.gotoList();
      },
      (error: any) => console.error()
    );
  }
  onSubmit() {
    this.submitted = true;
    this.save();
  }
  gotoList() {
    this.router.navigate(['/login']);
  }
}
  