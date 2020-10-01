# aws-ec2

 
A step-by-step on [Amazon EC2](https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud)

# Learning concepts: Notes from [Stéphane Maarek](https://www.udemy.com/course/aws-ec2-masterclass/)

## [What is EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

* EC2 is one of the most popular AWS offerings
* It mainly consist in the capability of:

1. Renting virtual machines (EC2).
1. Storing data on virtual drives (EBS).
1. Distributing load accros machines (ELB).
1. Scaling the services using an auto-scaling group (ASG).

* Knowing EC2 is fundamental to understand how the Cloud works.

## How to SSH and EC2 Instance?

* SSH is one of the most important functions. It allows you to control a remote machine, all using command line.

``` 
$ chmod 400 Your-Instance.pem
$ ssh -i ./Your-Folder/Your-Instance.pem ec2-user@Public-DNS.compute.amazonaws.com
```

* And much faster!
* Configure OpenSSH ~/.ssh/config -> facilitates the SSH into EC2 instances.

``` 
Host Your-Instance-Name
    Hostname Public-DNS.compute.amazonaws.com
    User ec2-user
    IdentityFile ~/Your-Folder/Your-Instance.pem
```

``` 
$ ssh Your-Instance-Name
```

### Exiting EC2

* Just type

``` 
$ exit
```

## Security groups

* They're fundamental for network security in AWS.
* They control how traffic is allowed/denied into/out the EC2 machines.
* It's the most fundamental skill to learn to troubleshoot networking issues.

## Private vs Public IP (IPv4)

* [IPv4](https://en.wikipedia.org/wiki/IPv4): It forms the Internet. It uses a logical addressing system and performs routing, which is the forwarding of packets from a source host to the next router that is one hop closer to the intended destination host on another network.

* Is still the most common format used online.

* Allows 3.7 billion different addresses in the public space

* [0-255].[0-255].[0-255].[0-255]

* [IPv6](https://en.wikipedia.org/wiki/IPv6): is the most recent version of the Internet Protocol (IP), the communications protocol that provides an identification and location system for computers on networks and routes traffic across the Internet.

* Is newer and solves problems for the IoT (Interner of Things)

* Comparisons with IPv4: The size of an IPv6 address is 128 bits, compared to 32 bits in IPv4.

### Public IP:

* Means that the machine can be identified on the internet (www)
* Must be unique across the whole web, *i.e.* two machines can't have the same public IP.
* Can be easily geo-located.

### Private IP:

* Means that the machine can be identified on a private network only
* IP must be unique across the private network.
* But two different private networks can have the same IP's.
* Machines connect to www using a proxy (an internet gateway).
* Only a specified range o IP's can be used as private IP.

### Therefore: By default, the EC2 machine comes with:

* A private IP for internal AWS Network.
* A public IP, for the www

### Lastly: When SSH the EC2 machine:

* We can't use a private IP, since we're not in the same network.
* We can only use the oublic IP.

### Moreover: If the EC2 machine stopped and then started over:

* The public IP can change.

``` 
$ ssh -i ./Your-Folder/Your-Instance.pem ec2-user@Public-IP
```

## EC2 User Data

* It is possible to bootstrap our instances using an EC2 User Data Script.
* Bootstrapping means lunching commands when a machine starts.
* That script only run once at the instance first start.
* EC2 User Data is used to automate boots tasks such as:

1. Installing updates
1. Installing softwaree
1. Downloading common files from the internet
1. Anything you can think of

## [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

* *E.g.*: t2.small in São Paulo costs US$0.0372 per Hour (using Linux)
* Then: X seconds (X>6), it costs US$0.0372*X/3600

## EC2 Images (AMI)

* AWS comes with base images such as:

1. Ubuntu
1. Fedora
1. RedHat
1. Windows
1. ...

* These images can be customized at runtime using EC2 User Data.
* However, we can create our own image -> That's an AMI! An image that we'll use to create our instances
* AMI's can be built for Linux or Windows machines.

### Why to use a custom AMI?

* Pre-installed packages needed.
* Faster boot time (no need for ec2 user at boot time).
* Machine comes configured with monitoring/enterprise software.
* Security concerns - control over the machines in the network.
* Control of maintenance and updates of AMIs over time.
* Active Directory Integration out of the box.
* Installing apps ahead of time (for faster deploys when auto-scaling).
* Using someone else's AMI that's optimised for running an app, DB...
* **AMIs are built for a specific AWS region!** 

### Using Public AMIs

* You can keverage AMIs from other people.
* You can also pay for other's AMI per hour:
1. These people have optimized the software.
1. The machine is easy to run and configure.
1. You basically rent "expertise" from the AMI creator.

* AMI can be found and published on the Amazon Marketplace.

* **WARNING!**:
1. Don't use an AMI you don't trust! (Pretty obvious, but it must be said.)
1. Some AMIs might come with malwares or may not be secure for enterprises.

### AMI Storage

* Your AMI take space and they live in Amazon S3
* Amazon S3 is a durable, cheap and resilient storage where most of your backuos will live (but you won't see them in the S3 console).
* By default: your AMIs are private and locked for your account/region.
* You can also make your AMIs public and share them with other AWS accounts or sell them on the AMI Marketplace.

### [AMI Pricing](https://aws.amazon.com/s3/pricing/)

* As mentioned above, AMIs live in Amazon S3, so you get charged for the __actual__ space it takes in Amazon S3.

* Amazon S3 Standard pricing in São Paulo:
1. First 50 TB/Month costs U$0.0405 per GB
1. Next 450 TB/Month costs U$0.039 per GB
1. Over 500 TB/Month costs U$0.037 per GB

* Overall it's quite cheap to store private AMIs.
* However, make sure to remove AMIs you don't use.

## [EC2 Instance Overview](https://aws.amazon.com/ec2/instance-types/)

For more [information](https://ec2instances.info/).

### Random Access Memory (RAM) (type, amount, generation)
* Is the computer "hot", because it doesn't persist.
* Is meant as an "speed-up" in a computer.
* Gets emptied and lost at each machine's reboot.

If RAM isn't large enough, you'll either get:
* OutOfMemory error
* The RAM will extend to the disk, *a.k.a* swapping, and performance may decrease considerably.

If you want to check the system's memory status:

```
$ free -m
```

For more details:

```
$ top
```
and press *Shift + f*, and now you're able to sort by whatever you like. 

Or you could also:

```
$ ps ux
```
or
```
$ ps u
```

### Central Process Unit (CPU) (type, make, frequency, generation, number of cores)
* Is a piece of hardware that carries out the instruction of a computer program.
* It performs the basic arithmatical, logical and input/output operations.
* Components
    * Multiple cores (independent, which enables multi-tasking)
    * Frequency. The higher the frequency means more computations in less time.

If the CPU isn't fast enough or doesn't have enough cores, then you'll get:
* CPU usage of each core at 100%.
* The server will seriously slow down.

### Input/Output (I/O) (disk performance, EBS optimizations)
* Is the concept or writing or reading from a disk.
* It's measured by:
    * Latency
    * Random I/O performance (random read/writes)
    * Sequential read or write performance
    * IOPS (I/O operations per second)

If the I/O isn't large enough, you'll get:
* Timeouts
* Slowdowns
* Crashes

### Network (bandwidth, latency)
* Is the concpet of how fast a  machine can send and receive information from other machines.
* It's measured by:
 * Latency
 * Throughput/Bandwidth

If your network isn't fast enough:
* Your application may time out.
* Latency may be induced.

Obs: Communication network amog EC2 machines is fast, but from outside is a bit slower.

### Graphical Processing Units (GPU)
* In a normal computer, it's used to compute the colour of the pixels on a screen.
* It's measured by:
    * Number of cores (sometimes well over 1024).
    * Internal GPU memory.

In AWS, the GPU is used to:
* process videos
* perform computation
* performa machine learning

## Network and Security

### Security groups
* Act as a "firewall"
* Regulate:
    * Access to port
    * Authorized of forbidden IP
    * Control of inbound network (from other to the instance)
    * Control of outbound network (from the instance to other)

**Good to know**
* Can be attached to multiple instances.
* Locked down to a region/VPC combination.
* Does live "outside" the EC2 - if traffic is blocked the EC2 instance won't see it.
* It's good to maintain one separate security group for SSH access.
* If your application isn't accessible (time-out), then it's a security group issue.
* If your application gives "connection refused" error, then it's an application error or it's not launched.
* All inbound traffic is blocked by default.
* All outbound traffic is authorized by deffault.

## Elastic Load Balancing

### What's load balancing?

* Load balancers are servers that forward internet traffic to multiple servers downstream.

### Why use a load balancer?

* Spread load across multiple downstream instances.
* Expose a single point of access (DNS) to your application.
* Seamlessly handle failures of downstream instances.
* Do regular health checks to your instances.
* Provide SSL termination (HTTPS) for your websites.
* Enforce availability across zones.
* Separate public traffic from provate traffic.