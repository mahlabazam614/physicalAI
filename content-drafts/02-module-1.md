---
sidebar_position: 2
---

# Module 1: The Robotic Nervous System (ROS 2)

## Focus
**Middleware for robot control.**

In this module, we explore the foundational "nervous system" of modern robotics: ROS 2 (Robot Operating System 2). Just as a nervous system transmits signals between the brain and muscles, ROS 2 handles communications between a robot's software algorithms and its physical hardware.

## Key Topics

### ROS 2 Nodes, Topics, and Services
-   **Nodes**: The fundamental processing units. Each node handles a specific task (e.g., reading a laser scanner, controlling a wheel motor).
-   **Topics**: The channels over which nodes exchange data. Publishers send data, Subscribers receive it.
-   **Services**: A request/reply communication pattern.

### Bridging Python Agents to ROS controllers using rclpy
We use `rclpy` (ROS Client Library for Python) to write our nodes. This allows us to integrate modern AI agents (written in Python) directly with the robot control stack.

### URDF (Unified Robot Description Format) for humanoids
-   Understanding the XML structure of URDF.
-   Defining links (rigid bodies) and joints (movable connections).
-   Visualizing the robot model in RViz.

## Weekly Breakdown

### Weeks 3-5: ROS 2 Fundamentals
-   ROS 2 architecture and core concepts
-   Nodes, topics, services, and actions
-   Building ROS 2 packages with Python
-   Launch files and parameter management

## Assessment
**ROS 2 package development project**: Create a custom package that launches a simulated robot and controls it via topic commands.
