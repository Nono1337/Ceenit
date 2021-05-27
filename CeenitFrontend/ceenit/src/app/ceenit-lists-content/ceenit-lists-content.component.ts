import { Component, OnInit } from '@angular/core';
import { Movie } from '../Model/movie.model';
import { HttpServiceService } from 'src/app/service/http-service.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-ceenit-lists-content',
  templateUrl: './ceenit-lists-content.component.html',
  styleUrls: ['./ceenit-lists-content.component.css']
})
export class CeenitListsContentComponent implements OnInit {

  ListContent : Movie[];
  constructor(private httpServe: HttpServiceService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.ListContent = new Array<Movie>();
    this.httpServe
      .getListMoviesByTitle(this.route.snapshot.paramMap.get('title'))
      .subscribe((resp) => {
        console.log(resp);
        if (resp != undefined) {
          // @ts-ignore: TS2339
          resp.forEach((movie) => {
            this.ListContent.push(movie);
          });
        }
      });
  }


}
