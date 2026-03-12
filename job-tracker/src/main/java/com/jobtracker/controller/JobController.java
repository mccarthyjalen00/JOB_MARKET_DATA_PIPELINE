package com.jobtracker.controller;

import com.jobtracker.model.Job;
import com.jobtracker.service.JobService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/jobs")
public class JobController {

    private final JobService service;

    public JobController(JobService service) {
        this.service = service;
    }

    @GetMapping
    public List<Job> getJobs(){
        return service.getAllJobs();
    }

    @PostMapping
    public Job createJob(@RequestBody Job job){
        return service.saveJob(job);
    }

    @DeleteMapping("/{id}")
    public void deleteJob(@PathVariable Long id){
        service.deleteJob(id);
    }

}