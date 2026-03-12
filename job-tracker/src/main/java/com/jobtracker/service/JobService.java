package com.jobtracker.service;

import com.jobtracker.model.Job;
import com.jobtracker.repository.JobRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobService {

    private final JobRepository repository;

    public JobService(JobRepository repository) {
        this.repository = repository;
    }

    public List<Job> getAllJobs(){
        return repository.findAll();
    }

    public Job saveJob(Job job){
        return repository.save(job);
    }

    public void deleteJob(Long id){
        repository.deleteById(id);
    }
}