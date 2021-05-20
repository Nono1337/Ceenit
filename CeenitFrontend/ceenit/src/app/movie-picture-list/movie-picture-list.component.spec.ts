import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoviePictureListComponent } from './movie-picture-list.component';

describe('MoviePictureListComponent', () => {
  let component: MoviePictureListComponent;
  let fixture: ComponentFixture<MoviePictureListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoviePictureListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MoviePictureListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
