import os
import time
import psutil
import random
import threading
import subprocess
import speedtest
import logging
import json
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import numpy as np
import requests
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PodPerformanceStressTester:
    """
    A comprehensive performance stress testing utility for Kubernetes pods
    Provides various performance metrics and stress testing capabilities
    """
    def __init__(self, test_duration: int = 300, result_file: str = '/tmp/performance_results.json'):
        """
        Initialize the performance stress tester
        
        Args:
            test_duration (int): Duration of performance tests in seconds
            result_file (str): Path to store performance test results
        """
        self.test_duration = test_duration
        self.result_file = result_file
        self.results: Dict[str, Any] = {
            'iops_read': {},
            'iops_write': {},
            'iops_read_write': {},
            'throughput': {},
            'network': {},
            'resource_utilization': {}
        }

    def run_disk_iops_test(self, test_type: str = 'random') -> Dict[str, float]:
        """
        Perform disk IOPS (Input/Output Operations Per Second) testing
        
        Args:
            test_type (str): Type of test - 'random' or 'sequential'
        
        Returns:
            Dict with IOPS metrics
        """
        try:
            # Create a temporary test file
            test_file = f'/tmp/iops_test_{test_type}.bin'
            file_size = 1 * 1024 * 1024 * 1024  # 1GB test file
            
            # Generate random or sequential data
            if test_type == 'random':
                data = os.urandom(4096)  # 4KB random data chunks
            else:
                data = bytes(range(256)) * (4096 // 256)  # Sequential data
            
            start_time = time.time()
            write_ops = 0
            read_ops = 0
            
            # Perform write operations
            with open(test_file, 'wb') as f:
                while time.time() - start_time < self.test_duration:
                    f.write(data)
                    f.flush()
                    write_ops += 1
            
            # Perform read operations
            with open(test_file, 'rb') as f:
                while time.time() - start_time < self.test_duration * 2:
                    f.read(4096)
                    read_ops += 1
            
            # Clean up test file
            os.remove(test_file)
            
            # Calculate IOPS
            write_iops = write_ops / (time.time() - start_time)
            read_iops = read_ops / (time.time() - start_time)
            
            return {
                'write_iops': write_iops,
                'read_iops': read_iops,
                'test_type': test_type
            }
        
        except Exception as e:
            logger.error(f"IOPS Test Failed: {e}")
            return {}

    def network_performance_test(self) -> Dict[str, float]:
        """
        Perform network performance testing
        
        Returns:
            Dict with network performance metrics
        """
        try:
            # Initialize speedtest
            st = speedtest.Speedtest()
            
            # Measure download speed
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            
            # Measure upload speed
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            
            # Measure ping
            st.get_best_server()
            ping = st.results.ping
            
            return {
                'download_speed_mbps': download_speed,
                'upload_speed_mbps': upload_speed,
                'ping_ms': ping
            }
        
        except Exception as e:
            logger.error(f"Network Performance Test Failed: {e}")
            return {}

    def cpu_memory_metrics(self) -> Dict[str, float]:
        """
        Collect pod-level CPU and memory metrics
        
        Note: This method attempts to gather metrics specific to the current process
        
        Returns:
            Dict with CPU and memory utilization
        """
        try:
            # Get current process
            current_process = psutil.Process()
            
            # CPU metrics
            cpu_percent = current_process.cpu_percent(interval=1)
            
            # Memory metrics (RSS - Resident Set Size)
            memory_info = current_process.memory_info()
            memory_usage_mb = memory_info.rss / (1024 * 1024)
            
            return {
                'cpu_percent': cpu_percent,
                'memory_usage_mb': memory_usage_mb
            }
        
        except Exception as e:
            logger.error(f"Resource Metrics Collection Failed: {e}")
            return {}

    def run_comprehensive_tests(self):
        """
        Execute all performance tests and aggregate results
        """
        # Random and Sequential IOPS Tests
        self.results['iops_read']['random'] = self.run_disk_iops_test('random')
        self.results['iops_read']['sequential'] = self.run_disk_iops_test('sequential')
        
        # Network Performance Test
        self.results['network'] = self.network_performance_test()
        
        # CPU and Memory Metrics
        self.results['resource_utilization'] = self.cpu_memory_metrics()
        
        # Save results to file
        with open(self.result_file, 'w') as f:
            json.dump(self.results, f, indent=4)
        
        logger.info("Comprehensive Performance Tests Completed")

# Flask Web Application for Results Visualization
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    """
    Render the main performance dashboard
    """
    return render_template('performance_dashboard.html')

@app.route('/performance-data')
def get_performance_data():
    """
    API endpoint to fetch performance test results
    """
    try:
        with open('/tmp/performance_results.json', 'r') as f:
            results = json.load(f)
        return jsonify(results)
    except FileNotFoundError:
        return jsonify({"error": "Performance tests not run yet"})

def run_performance_tests():
    """
    Background thread to run performance tests periodically
    """
    while True:
        tester = PodPerformanceStressTester()
        tester.run_comprehensive_tests()
        time.sleep(300)  # Run tests every 5 minutes

if __name__ == '__main__':
    # Start performance testing in a background thread
    test_thread = threading.Thread(target=run_performance_tests)
    test_thread.daemon = True
    test_thread.start()
    
    # Run Flask application
    socketio.run(app, host='0.0.0.0', port=5000)
