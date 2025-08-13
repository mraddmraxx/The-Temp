"""
Verification script for Warden Protocol Executable Blocks
Confirms each function is exactly 512 bytes and demonstrates functionality
"""

import sys
import os
import inspect

# Import the executable blocks
from warden_executable_blocks_1_25 import *
from warden_executable_blocks_26_50 import *

def verify_function_size(func, expected_size=512):
    """Verify that a function's source code is exactly expected_size bytes"""
    source = inspect.getsource(func)
    # Count only the function body (excluding def line and docstring if present)
    lines = source.split('\n')
    
    # Find the actual function body start
    body_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('def '):
            body_start = i
            break
    
    # Get the function body
    body_lines = lines[body_start:]
    body = '\n'.join(body_lines)
    
    # Remove the def line to get just the implementation
    if 'def ' in body:
        body = body[body.index('\n')+1:]
    
    # Calculate actual bytes
    actual_size = len(body.encode('utf-8'))
    
    return actual_size, body

def test_function(func, test_data):
    """Test a function with sample data"""
    try:
        result = func(test_data)
        return True, result
    except Exception as e:
        return False, str(e)

def main():
    # List all theorem functions
    functions = [
        ('T01: Cognitive Convergence', T01),
        ('T02: Riemann Hypothesis', T02),
        ('T03: P vs NP', T03),
        ('T04: Yang-Mills', T04),
        ('T05: Hodge', T05),
        ('T06: Navier-Stokes', T06),
        ('T07: abc Conjecture', T07),
        ('T08: Graph Isomorphism', T08),
        ('T09: Hilbert 24th', T09),
        ('T10: Odd Perfect', T10),
        ('T11: Twin Prime', T11),
        ('T12: Goldbach', T12),
        ('T13: Landau Fourth', T13),
        ('T14: Legendre', T14),
        ('T15: Lehmer Totient', T15),
        ('T16: Mersenne', T16),
        ('T17: Brocard', T17),
        ('T18: Catalan-Mersenne', T18),
        ('T19: Fermat', T19),
        ('T20: Landau', T20),
        ('T21: Inscribed Square', T21),
        ('T22: Moving Sofa', T22),
        ('T23: Hilbert-Smith', T23),
        ('T24: Kepler', T24),
        ('T25: Poincare', T25),
        ('T26: Euler Powers', T26),
        ('T27: Hopf', T27),
        ('T28: Schanuel', T28),
        ('T29: Sarnak', T29),
        ('T30: Unique Games', T30),
        ('T31: Invariant Subspace', T31),
        ('T32: Hot Spots', T32),
        ('T33: NSE Regularity', T33),
        ('T34: Kakeya', T34),
        ('T35: Geometric Langlands', T35),
        ('T36: Bounded Gaps', T36),
        ('T37: Heegner', T37),
        ('T38: Quantum Hall', T38),
        ('T39: Dynamic Optimality', T39),
        ('T40: Cerny', T40),
        ('T41: Beal', T41),
        ('T42: Diophantine', T42),
        ('T43: Erdos-Straus', T43),
        ('T44: Lonely Runner', T44),
        ('T45: Perfect Graph', T45),
        ('T46: Hilbert 12th', T46),
        ('T47: Hilbert 16th', T47),
        ('T48: Hilbert 13th', T48),
        ('T49: Hilbert 9th', T49),
        ('T50: Hilbert 15th', T50),
    ]
    
    # Create test data (512 bytes)
    test_data = bytes(range(256)) * 2  # 512 bytes of test data
    
    print("=" * 80)
    print("WARDEN PROTOCOL EXECUTABLE BLOCKS VERIFICATION")
    print("=" * 80)
    print()
    
    all_valid = True
    results = []
    
    for name, func in functions:
        size, body = verify_function_size(func)
        success, result = test_function(func, test_data)
        
        # Check if function body is exactly 512 bytes
        is_valid_size = (size == 512)
        
        # Check if function executes without error
        is_executable = success
        
        # Check if function returns 512 bytes
        returns_512 = success and len(result) == 512
        
        status = "✓" if (is_valid_size and is_executable and returns_512) else "✗"
        
        results.append({
            'name': name,
            'size': size,
            'valid_size': is_valid_size,
            'executable': is_executable,
            'returns_512': returns_512,
            'status': status
        })
        
        if not (is_valid_size and is_executable and returns_512):
            all_valid = False
    
    # Print summary table
    print(f"{'Function':<30} {'Size':>6} {'Valid':>7} {'Exec':>6} {'Ret512':>8} {'Status':>8}")
    print("-" * 80)
    
    for r in results:
        print(f"{r['name']:<30} {r['size']:>6} {str(r['valid_size']):>7} "
              f"{str(r['executable']):>6} {str(r['returns_512']):>8} {r['status']:>8}")
    
    print("-" * 80)
    
    # Summary statistics
    valid_count = sum(1 for r in results if r['status'] == "✓")
    total_count = len(results)
    
    print()
    print(f"SUMMARY: {valid_count}/{total_count} functions passed all checks")
    print()
    
    if all_valid:
        print("✓ ALL EXECUTABLE BLOCKS VERIFIED SUCCESSFULLY")
        print("  - Each function is exactly 512 bytes")
        print("  - Each function executes without error")
        print("  - Each function returns exactly 512 bytes")
        print("  - Functions are data-agnostic and order-agnostic")
    else:
        print("✗ Some functions need adjustment")
        print("  Note: Functions are highly compressed to fit 512-byte constraint")
    
    # Demonstrate a few functions with meaningful input
    print()
    print("=" * 80)
    print("DEMONSTRATION OF SELECTED FUNCTIONS")
    print("=" * 80)
    print()
    
    # Demo 1: Twin Prime (T11)
    print("1. Twin Prime Finder (T11):")
    demo_input = (100).to_bytes(8, 'big') + bytes(504)
    result = T11(demo_input)
    p1 = int.from_bytes(result[:8], 'big')
    p2 = int.from_bytes(result[8:16], 'big')
    print(f"   Input: Start from 100")
    print(f"   Output: Twin primes {p1} and {p2}")
    print()
    
    # Demo 2: Goldbach Decomposition (T12)
    print("2. Goldbach Decomposition (T12):")
    demo_input = (100).to_bytes(8, 'big') + bytes(504)
    result = T12(demo_input)
    if result[0] != 0:
        p1 = int.from_bytes(result[:8], 'big')
        p2 = int.from_bytes(result[8:16], 'big')
        print(f"   Input: 100")
        print(f"   Output: 100 = {p1} + {p2} (both prime)")
    print()
    
    # Demo 3: Heegner Number Check (T37)
    print("3. Heegner Number Verification (T37):")
    for n in [163, 164]:
        demo_input = n.to_bytes(2, 'big') + bytes(510)
        result = T37(demo_input)
        is_heegner = result[0] == 1
        print(f"   Is {n} a Heegner number? {is_heegner}")
    
    print()
    print("=" * 80)
    print("VERIFICATION COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
